##raster_WEVector=name
##inputraster=raster
##wevectorlayer=output vector
outputs_GDALOGRTILEINDEX_1=processing.runalg('gdalogr:tileindex', [inputraster],'location',False,None)
outputs_QGISREPROJECTLAYER_1=processing.runalg('qgis:reprojectlayer', outputs_GDALOGRTILEINDEX_1['OUTPUT'],'EPSG:4326',wevectorlayer)