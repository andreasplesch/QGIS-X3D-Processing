'''QGIS Processing script
(c) 2017 Andreas Plesch
extracts and returns color ramp as SFImage from raster layer
or custom ramp if requested
'''
##X3D=group
##SFImage string from color_ramp=name
##input_raster=raster
##extract_color_ramp=boolean True
##custom_ramp=string 3 1 1 0x00 0x80 0xff
##output_SFImage_string=output string

r = processing.getObject(input_raster)
output_SFImage_string = custom_ramp
if extract_color_ramp:
    renderer = r.renderer()
    if renderer.type() == 'singlebandpseudocolor':
        colorList = renderer.shader().rasterShaderFunction().colorRampItemList()
        out = "%s 1 4 " % len(colorList)
        hexColors = [ "0x%02x%02x%02x%02x" % (c.red(),c.green(),c.blue(),c.alpha()) for c in [x.color for x in colorList]]
        out+= " ".join(hexColors)
        output_SFImage_string = out
print(output_SFImage_string)

