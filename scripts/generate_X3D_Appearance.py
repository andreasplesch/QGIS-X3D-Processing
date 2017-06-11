'''
QGIS processing script
(c) 2017 Andreas Plesch
generate a XML encoded X3D Appearance node with a color
or a PixelTexture or a ImageTexture
'''
##X3D=group
##generate X3D Appearance=name
##ambientIntensity=number 0.2
##diffuseColor=string 0.8 0.8 0.8 
##emissiveColor=string 0 0 0
##shininess=number 0.2
##specularColor=string 0 0 0
##transparency=number 0
##use_ImageTexture=string False
##ImageTexture_url=string textures/exampleImagery.jpg
##use_PixelTexture=string False
##PixelTexture=string 3 1 1 0x00 0x80 0xff
##magnificationFilter=string NEAREST_PIXEL
##output_string=output string

ambientIntensityDefault = 0.2
diffuseColorDefault = '0.8 0.8 0.8'
emissiveColorDefault = '0 0 0'
shininessDefault = 0.2
specularColorDefault = '0 0 0'
transparencyDefault = 0

out='<Appearance>'
out+='<Material'

if ambientIntensity != ambientIntensityDefault:
    out+=" ambientIntensity='%s'" % ambientIntensity
if diffuseColor != diffuseColorDefault:
    out+=" diffuseColor='%s'" % diffuseColor
if emissiveColor != emissiveColorDefault:
    out+=" emissiveColor='%s'" % emissiveColor
if specularColor != specularColorDefault:
    out+=" specularColor='%s'" % specularColor
if shininess != shininessDefault:
    out+=" shininess='%s'" % shininess
if transparency != transparencyDefault:
    out+=" transparency='%s'" % transparency

out+='></Material>'

if use_ImageTexture == 'True':
    out+='<ImageTexture url="%s">' % ImageTexture_url
    out+='</ImageTexture>'

elif use_PixelTexture == 'True':
    out+='<PixelTexture image="%s">' % PixelTexture
    out+='  <TextureProperties boundaryModeS="CLAMP" boundaryModeT="CLAMP" magnificationFilter="%s"></TextureProperties>' % magnificationFilter
    out+='</PixelTexture>'

out+='</Appearance>'

output_string = out
#print(out)