'''
QGIS Processing script
(c) 2017 Andreas Plesch
convert DEM layer to xml encoded X3D TextureCoordinate node
with interval normalized heights as U and zero V
to use with 1d texture
'''

##X3D=group
##TextureCoordinate_from_DEM=name
##DEM_raster_layer=raster
##intervals=string 100 200
##significant_digits_in_output=number 3
##X3D_TextureCoordinate_file=output file

#import os.path
#from qgis.PyQt.QtCore import QDateTime
#from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException

# constants
MAXDIM=1000 # X3D is all text
LINELENGTH=80 # make shorter lines
# try to use standard qgis interface
r = processing.getObject(DEM_raster_layer)

rData = r.dataProvider()
noDataValue = -99999
ndvs=rData.userNoDataValues(1) # always first band
if rData.srcHasNoDataValue(1): noDataValue = rData.srcNoDataValue(1) # by default use original source ndv
if ndvs and not rData.useSrcNoDataValue(1): noDataValue = ndvs[0].min() # if user defined ndata use one

xDimension = r.width()
zDimension = r.height()
# must be raster
# check if too large, warn
if xDimension * zDimension > MAXDIM * MAXDIM:
    progress.setText('<b>Raster may be too large: %s values, but trying</b>' % xDimension*zDimension)

f = open(X3D_TextureCoordinate_file, 'w')

f.write( "<TextureCoordinate point='\n" )

# height
values = processing.scanraster(r, progress) # reads only one line into memory
i = 0
intervalList = [float(x) for x in intervals.split()]
n_intervals = len(intervalList)
for v in values:
    if v is None: v = noDataValue
    #find interval
    intervalIndex = len([x for x in intervalList if x < v])
    u = 1
    #intervalwise normalization
    if intervalIndex < n_intervals:
        intervalMax = intervalList[intervalIndex]
        intervalMin = intervalList[max(intervalIndex-1, 0)]
        intervalRange = intervalMax - intervalMin
        u = 0
        if intervalRange > 0:
            u = min(max((v - intervalMin)/intervalRange, 0), 1)
            u = (intervalIndex + u)/n_intervals
    f.write( "%.*G 0," % (int(significant_digits_in_output), u))
    i += 1
    if i % LINELENGTH == 0: f.write( "\n" )
f.write( "'>\n" )
#f.write( ">\n" )

f.write( "  <MetadataSet name='height texture metadata' >\n")
f.write( "    <MetadataString name='intervals' value='\"%s\"' ></MetadataString>\n" % intervals )
f.write( "    <MetadataString name='generator' value='QGIS Processing' ></MetadataString>\n" )
f.write ( "  </MetadataSet>\n")

f.write( "</TextureCoordinate>" )

f.close()
