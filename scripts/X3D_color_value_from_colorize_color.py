'''
QGIS Processing script
(c) 2017 Andreas Plesch
extracts and returns colorize color as string from raster layer
or custom color if requested
'''
##X3D=group
##color string from colorize color=name
##input_raster=raster
##extract_colorize_color=boolean True
##custom_color=string 0.8 0.8 0.7
##output_color_string=output string

r = processing.getObject(input_raster)
output_color_string = custom_color  # needs some sanity checking
if extract_colorize_color:
    colorize = r.hueSaturationFilter().colorizeColor()
    output_color_string = '%s %s %s' % (colorize.redF(), colorize.greenF(), colorize.blueF())
print(output_color_string)
