'''QGIS Processing script
(c) 2017 Andreas Plesch
clip/expand raster to extent of other raster, warp
'''
##X3D=group
##clip_and_warp=name
##imagery=raster
##dem=raster
##clipped_imagery=output raster

dem_bounds = processing.runalg('modelertools:rasterlayerbounds', dem)
d = processing.getObject(dem)

tsrs = d.crs().toWkt()

#use warp and te instead
clipped_imagery = processing.runalg('gdalogr:warpreproject', imagery, '', tsrs, None, 0.0, 0, True, dem_bounds['EXTENT'],'', 5, 4, 75.0, 6.0, 1.0, False, 0, False, None, None)['OUTPUT']