'''QGIS Processing script
(c) 2017 Andreas Plesch
checks if raster renderer is single band pseudo color
and therefore has a color ramp
'''
##X3D=group
##is_singlebandpseudocolor=name
##input_raster=raster
##output_isSingleBandPseudoColor=output string
r = processing.getObject(input_raster)
#need string as output type since boolean is not available
output_isSingleBandPseudoColor = str(r.renderer().type() == 'singlebandpseudocolor')
