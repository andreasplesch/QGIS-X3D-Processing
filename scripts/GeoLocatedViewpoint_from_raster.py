##X3D=group
##GeoLocated Viewpoint from raster=name
##input_raster=raster
##mode=selection map; north
##centerOfRotation_height=number 0
##output_viewpoint_file=output file
##output_viewpoint_string=output string

#import math

majorR = 6378137
f = 298.257223563
minorR = majorR * ( 1 - 1/f ) + centerOfRotation_height
LAT2METER = 2 * 3.14 * minorR / 360

#r=processing.getObject(input_raster)
#use tile index processing to generate outline
#use reproject layer to reproject to GD WE = epsg:4326
outline = processing.runalg( 'gdalogr:tileindex', [input_raster], 'location', False, None)
outlineWE = processing.runalg( 'qgis:reprojectlayer', outline['OUTPUT'],'EPSG:4326', None)
o = processing.getObject(outlineWE['OUTPUT'])

e = o.extent()
centerPoint = e.center()
height = e.height() * LAT2METER

'''
cRad = (math.radians(centerPoint.x()), math.radians(centerPoint.y()))
latR = minorR * math.cos(cRad[1])
cor = (
    latR * math.cos(cRad[0]),
    latR * math.sin(cRad[0]),
    minorR * math.sin(cRad[1])
)
'''

cor = (0, -height +centerOfRotation_height, 0) 

orientation = '1 0 0 -1.57' #down

description = 'map view'

DEF = 'mapVP'
GeoDEF = 'geoMapVP'

out = "<GeoLocation DEF='%s' geoCoords='%s %s %s'>\n" % (GeoDEF, centerPoint.y(), centerPoint.x(), height)
out+= "  <Viewpoint DEF='%s'\n" % DEF
out+= "    description='%s'\n" % description
#out+= "    position='%s %s %s'\n" % (centerPoint.y(), centerPoint.x(), height)
out+= "    orientation='%s'\n" % orientation
out+= "    centerOfRotation='%s %s %s'" % cor
#out+= ' geoSystem=\'"GD" "WE"\'\n ' # default
out+= "  >\n  </Viewpoint>\n"
out+= "</GeoLocation>\n"


f=open(output_viewpoint_file, 'w')
f.write(out)
f.close()

output_viewpoint_string = out
print(out)
