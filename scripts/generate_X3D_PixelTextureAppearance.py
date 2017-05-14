'''
QGIS processing script
(c) 2017 Andreas Plesch
generate a XML encoded X3D Appearance node with a PixelTexture
'''
##X3D=group
##generate X3D PixelTexture Appearance=name
##pixelTexture=string 3 1 1 0x00 0x80 0xff
##magnificationFilter=string NEAREST_PIXEL
##output_string=output string

out="<Appearance>"

out+="<Material></Material>"

out+='<PixelTexture image="%s">' % pixelTexture
out+='  <TextureProperties boundaryModeS="CLAMP" boundaryModeT="CLAMP" magnificationFilter="%s"></TextureProperties>' % magnificationFilter
out+='</PixelTexture>'

out+='</Appearance>'

output_string = out
print(out)