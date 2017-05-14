'''QGIS Processing script
(c) 2017 Andreas Plesch
extracts and returns color ramp as SFImage from raster layer
as well as interpolation type as magnification filter
and interval boundaries as string
or custom values if requested
'''
##X3D=group
##X3D_color_ramp=name
##input_raster=raster
##extract_color_ramp=boolean True
##custom_ramp=string 3 1 1 0x00 0x80 0xff
##custom_boundaries=string 0 500 1000
##custom_interpolation=selection DISCRETE;INTERPOLATED  
##output_SFImage_string=output string
##output_boundaries_string=output string
##output_magFilter=output string
r = processing.getObject(input_raster)
output_SFImage_string = custom_ramp
output_boundaries_string = custom_boundaries
rampType2magFilter={'DISCRETE':'NEAREST_PIXEL', 'INTERPOLATED':'DEFAULT'}
rampTypes=rampType2magFilter.keys()
rampType = rampTypes[custom_interpolation]
if extract_color_ramp:
    renderer = r.renderer()
    if renderer.type() == 'singlebandpseudocolor':
        shaderFunction = renderer.shader().rasterShaderFunction()
        rampType = shaderFunction.colorRampTypeAsQString()
        if rampType not in rampTypes: rampType = rampTypes[0]
        colorList = shaderFunction.colorRampItemList()
        out = "%s 1 4 " % len(colorList)
        hexColors = [ "0x%02x%02x%02x%02x" % (c.red(), c.green(), c.blue(), c.alpha()) for c in [x.color for x in colorList]]
        out+= " ".join(hexColors)
        output_SFImage_string = out
        out = [str(x.value) for x in colorList]
        output_boundaries_string = " ".join(out)
output_magFilter=rampType2magFilter[rampType]
print(output_SFImage_string, output_boundaries_string, output_magFilter)

