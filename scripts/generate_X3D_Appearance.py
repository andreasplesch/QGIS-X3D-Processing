'''
QGIS processing script
(c) 2017 Andreas Plesch
generate a XML encoded X3D Appearance node with a color
or a PixelTexture
'''
##X3D=group
##generate X3D Appearance=name
##ambientIntensity=number 0.2
##diffuseColor=string 0.8 0.8 0.8 
##emissiveColor=string 0 0 0
##shininess=number 0.2
##specularColor=string 0 0 0
##transparency=number 0
##use_PixelTexture=string False
##pixelTexture=string 3 1 1 0x00 0x80 0xff
##magnificationFilter=string NEAREST_PIXEL
##output_string=output string

ambientIntensityDefault = 0.2
diffuseColorDefault = '0.8 0.8 0.8'
emissiveColorDefault = '0 0 0'
shininessDefault = 0.2
specularColorDefault = '0 0 0'
transparencyDefault = 0

Out='<Appearance>'
Out+='<Material'

if ambientIntensity != ambientIntensityDefault:
    Out+=" ambientIntensity='%s'" % ambientIntensity
if diffuseColor != diffuseColorDefault:
    Out+=" diffuseColor='%s'" % diffuseColor
if emissiveColor != emissiveColorDefault:
    Out+=" emissiveColor='%s'" % emissiveColor
if specularColor != specularColorDefault:
    Out+=" specularColor='%s'" % specularColor
if shininess != shininessDefault:
    Out+=" shininess='%s'" % shininess
if transparency != transparencyDefault:
    Out+=" transparency='%s'" % transparency

Out+='></Material>'

if use_PixelTexture == 'True':
    Out+='<PixelTexture image="%s">' % pixelTexture
    Out+='  <TextureProperties boundaryModeS="CLAMP" boundaryModeT="CLAMP" magnificationFilter="%s"></TextureProperties>' % magnificationFilter
    Out+='</PixelTexture>'

Out+='</Appearance>'

output_string = Out
#print(Out)