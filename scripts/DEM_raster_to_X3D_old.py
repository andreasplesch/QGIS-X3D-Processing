##X3D=group
##DEM_raster_layer=raster
##vertical_exaggeration=number 1
##significant_digits_in_output=number 6
##X3D_GeoElevationGrid_file=output file
from qgis.PyQt.QtCore import QDateTime
from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException

# constants
MAXDIM=10000 # X3D is all text
X3DProjections={'utm':'UTM', 'longlat':'GD'} # as 'Acronyms'
X3DEllipsoids = { # http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/components/geodata.html#t-earthellipsoids
(6377563.396, 299.3249646): 'AA', # Airy 1830
(6377340.189, 299.3249646): 'AM', # Modified Airy
(6378160, 298.25): 'AN', # Australian National	
(6377483.865, 299.1528128): 'BN', # Bessel 1841 (Namibia)
(6377397.155, 299.1528128): 'BR', # Bessel 1841 (Ethiopia Indonesia...)
(6378206.4, 294.9786982): 'CC', # Clarke 1866
(6378249.145, 293.465): 'CD', #	Clarke 1880
(6377276.345, 300.8017): 'EA', # Everest (India 1830)
(6377298.556, 300.8017): 'EB', # Everest (Sabah & Sarawak)
(6377301.243, 300.8017): 'EC', # Everest (India 1956)
(6377295.664, 300.8017): 'ED', # Everest (W. Malaysia 1969)
(6377304.063, 300.8017): 'EE', # Everest (W. Malaysia & Singapore 1948)
(6377309.613, 300.8017): 'EF', # Everest (Pakistan)
(6378155, 298.3): 'FA', # Modified Fischer 1960
(6378200, 298.3): 'HE', # Helmert 1906
(6378270, 297): 'HO', # Hough 1960
(6378160, 298.247): 'ID', # Indonesian 1974
(6378388, 297): 'IN', # International 1924
(6378245, 298.3): 'KA', # Krassovsky 1940
(6378137, 298.257222101): 'RF', # Geodetic Reference System 1980 (GRS 80)
(6378160, 298.25): 'SA', # South American 1969
(6378135, 298.26): 'WD', # WGS 72
(6378137, 298.257223563): 'WE' # WGS 84
}

# try to use standard qgis interface
r = processing.getObject(DEM_raster_layer)

rData = r.dataProvider()
noDataValue = -99999
ndvs=rData.userNoDataValues(1) # always first band
if rData.srcHasNoDataValue(1): noDataValue = rData.srcNoDataValue(1) # by default use original source ndv
if ndvs and not rData.useSrcNoDataValue(1): noDataValue = ndvs[0].min() # if user defined ndata use one

xDimension = r.width()
zDimension = r.height()
xSpacing = r.rasterUnitsPerPixelX()
zSpacing = r.rasterUnitsPerPixelY()

crsDescription = r.crs().description()
crsWkt = r.crs().toWkt()
crsProjection = r.crs().projectionAcronym()

# sanity checks
# must be raster
# check if too large, warn
if xDimension * zDimension > MAXDIM * MAXDIM:
    progress.setText('<b>Raster may be too large: %s values, but trying</b>' % xDimension*zDimension)
# check if crs not GD or UTM, bail
# crs().projectionAcronym() = 'longlat' -> GD
# = 'utm' -> UTM
if crsProjection not in X3DProjections.keys():
    raise GeoAlgorithmExecutionException('%s projection not supported by X3D. Reproject to longlat or UTM first.' % crsProjection)

# construct geoSystem string

projection =  X3DProjections[crsProjection] # start with projection

geoSystem = [ projection ]

if projection == 'UTM':
    zone = 'Z'
    zoneNo = crsDescription[crsDescription.rfind(' '):].strip() # after last space, has N or S suffix
    zone += zoneNo[0:-1]
    geoSystem.append(zone)
    geoSystem.append(zoneNo[-1]) # N or S

# ellipsoid: directly from major axis, flattening values, mapped to 2 letter code
# get major axis, flattengin from wkt SPHEROID:
# spheroid=[float(str) for str in crsWkt[crsWkt.find('SPHEROID'):].split(',')[1:3]] # 'major axis', 'flattening'
# then use dictionary to lookup code:

spheroid = [float(str) for str in crsWkt[crsWkt.find('SPHEROID'):].split(',')[1:3]] # 'major axis', 'flattening'
spheroidTuple = (spheroid[0], spheroid[1]) # works, but perhaps add some rounding round(s*1e9)/1e9
if spheroidTuple not in X3DEllipsoids.keys():
    raise GeoAlgorithmExecutionException('%s spheroid not supported by X3D. Reproject to WGS84 first.' % crsDescription)

ellipsoidCode = X3DEllipsoids[spheroidTuple] # see above

geoSystem.append(ellipsoidCode)
    
gS = ['"%s"' % s for s in geoSystem] # add double quotes for multi string

# origin
e = r.extent()
geoGridOrigin = [e.xMinimum(), e.yMaximum(), 0] # values are provided starting from NW corner

# other fields as input: yScale, solid, ...

# height
values = processing.scanraster(r, progress)

f = open(X3D_GeoElevationGrid_file, 'w')

# debug
f.write( "<GeoElevationGrid\n" )
f.write( "  geoGridOrigin='%f %f %f'\n" % (geoGridOrigin[1], geoGridOrigin[0],  geoGridOrigin[2]) )
f.write( "  xDimension='%d'\n" % xDimension)
f.write( "  zDimension='%d'\n" % zDimension)
f.write( "  xSpacing='%f'\n" % xSpacing )
f.write( "  zSpacing='%f'\n" % -zSpacing ) # need to reverse since starting from NW, flipped normals
f.write( "  solid='false'\n" ) # need to show backface
f.write( "  yScale='%s'\n" % vertical_exaggeration )
if geoSystem != ['GD','WE']:
    f.write( "  geoSystem='%s'\n" % " ".join(gS) )
f.write( "  height=' ")
for v in values:
    if v is None: v = noDataValue
    f.write( "%.*G " % (int(significant_digits_in_output), v))
f.write( "'>\n" )
#f.write( ">\n" )

f.write( "  <MetadataSet name='Raster metadata' >\n")
f.write( "    <MetadataString name='title' value='%s' ></MetadataString>\n" % r.name() )
f.write( "    <MetadataString name='attribution' value='%s' ></MetadataString>\n" % r.attribution() )
f.write( "    <MetadataString name='attributionReference' value='%s' ></MetadataString>\n" % r.attributionUrl() )
f.write( "    <MetadataString name='generator' value='QGIS Processing DEM_raster_to_X3D.py' ></MetadataString>\n" )
now = QDateTime.currentDateTime()
f.write( "    <MetadataString name='generated' value='%s' ></MetadataString>\n" % now.toString() )
f.write ( "  </MetadataSet>\n")

f.write( "</GeoElevationGrid>" )

f.close()
