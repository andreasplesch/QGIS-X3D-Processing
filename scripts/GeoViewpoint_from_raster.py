'''
constructs a X3D GeoViewpoint which shows a raster in top down map or other  views
(c) 2017 Andreas Plesch
'''
##X3D=group
##GeoViewpoint from raster=name
##input_raster=raster
##mode=selection map;north;west;south;east
##centerOfRotation_height=number 0
##output_geoviewpoint_file=output file
##output_geoviewpoint_string=output string

import math

fov = 45 # default fov
r675 = math.radians(90-fov/2)
#r225 = math.radians(fov/2)
#c225 = math.cos(r225)
#s225 = math.sin(r225)
t675 = math.tan(r675)/2

modeMap = {0:'map', 1:'north', 2:'west', 3:'south', 4:'east'}
m=modeMap[mode]

mode2orientation = { #http://www.andre-gaschler.com/rotationconverter/
    'map':'1 0 0 -1.57', #down
    'north':'1 0 0 %s' % -r675, #to north
    'east':'-0.4859482 -0.7266942 -0.4855614 1.8839996', #(c225, s225),
    'south':'0 -0.8314697 -0.5555701 3.1415', # % (3.1415),
    'west':'-0.4859482 0.7266942 0.4855614 1.8839996' #% (1, 0) #(c225, -s225)
}

mode2description = {
    'map':'map view', 
    'north':'view to north', #to north
    'east':'view to east',
    'south':'view to south',
    'west':'view to west'
}

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
mheight = e.height() * LAT2METER * t675
mwidth = e.width() * LAT2METER * math.cos(math.radians(centerPoint.y())) * t675
height = max(mheight, mwidth)

'''
cRad = (math.radians(centerPoint.x()), math.radians(centerPoint.y()))
latR = minorR * math.cos(cRad[1])
cor = (
    latR * math.cos(cRad[0]),
    latR * math.sin(cRad[0]),
    minorR * math.sin(cRad[1])
)
'''

mode2position = {
    'map': (centerPoint.y(), centerPoint.x(), height),
    'north':(e.yMinimum(), centerPoint.x(), mheight),
    'east':(centerPoint.y(), e.xMinimum(), mwidth),
    'south':(e.yMaximum(), centerPoint.x(), mheight),
    'west':(centerPoint.y(), e.xMaximum(), mwidth)
}

position = mode2position[m]

orientation = mode2orientation[m]

description = mode2description[m]

DEF = description.replace(' ', '_')

out = "<GeoViewpoint DEF='%s'\n" % DEF
out+= "  description='%s'\n" % description
out+= "  position='%s %s %s'\n" % position
out+= "  orientation='%s'\n" % orientation
out+= "  centerOfRotation='%s %s %s'" % (centerPoint.y(), centerPoint.x(), centerOfRotation_height) #cor is geocentric
#out+= ' geoSystem=\'"GD" "WE"\'\n ' # default
out+= ">\n </GeoViewpoint>\n"

f=open(output_geoviewpoint_file, 'w')
f.write(out)
f.close()

output_geoviewpoint_string = out
#print(out)
