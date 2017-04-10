##X3D=group
##GeoLocation from raster center=name
##input_raster=raster
##output_GeoLocation_string=output string

#r=processing.getObject(input_raster)
#use tile index processing to generate outline
#use reproject layer to reproject to GD WE = epsg:4326
outline = processing.runalg( 'gdalogr:tileindex', [input_raster], 'location', False, None)
outlineWE = processing.runalg( 'qgis:reprojectlayer', outline['OUTPUT'],'EPSG:4326', None)
o = processing.getObject(outlineWE['OUTPUT'])

e = o.extent()
centerPoint = e.center()

DEF = 'mapCenter'

out = "<GeoLocation DEF='%s' geoCoords='%s %s %s'>\n" % (DEF, centerPoint.y(), centerPoint.x(), 0)
#add metadata
#name of raster, crs ...
out+= "</GeoLocation>\n"

#f=open(output_viewpoint_file, 'w')
#f.write(out)
#f.close()

output_GeoLocation_string = out
print(out)
