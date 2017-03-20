##X3D=group
##GeoViewpoint from raster=name
##input_raster=raster
##mode=selection map; north
##centerOfRotation_height=number 0
##output_geoviewpoint_file=output file
##output_geoviewpoint_string=output string

#import math

majorR = 6378137
f = 298.257223563
minorR = majorR * ( 1 - 1/f )
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
orientation = '1 0 0 -1.57' #down

description = 'map view'

DEF = 'mapVP'

out = "<GeoViewpoint DEF='%s'\n" % DEF
out+= "  description='%s'\n" % description
out+= "  position='%s %s %s'\n" % (centerPoint.y(), centerPoint.x(), height)
out+= "  orientation='%s'\n" % orientation
out+= "  centerOfRotation='%s %s %s'" % (centerPoint.y(), centerPoint.x(), centerOfRotation_height) # cor is geocentric, not needed
#out+= ' geoSystem=\'"GD" "WE"\'\n ' # default
out+= ">\n </GeoViewpoint>\n"

f=open(output_geoviewpoint_file, 'w')
f.write(out)
f.close()

output_geoviewpoint_string = out
#print(out)
