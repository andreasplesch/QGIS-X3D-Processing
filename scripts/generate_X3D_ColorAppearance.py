##X3D=group
##generate X3D color Appearance=name
##ambientIntensity=number 0.2
##diffuseColor=string 0.8 0.8 0.8 
##emissiveColor=string 0 0 0
##shininess=number 0.2
##specularColor=string 0 0 0
##transparency=number 0
##Out=output string

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
Out+='</Appearance>'

print(Out)