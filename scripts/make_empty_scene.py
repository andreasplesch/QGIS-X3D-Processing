##X3D=group
##make_empty_scene=name
##output_file=output file

f=open(output_file,'w')
f.write('''<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 3.0//EN" "http://www.web3d.org/specifications/x3d-3.0.dtd">
<X3D profile='Immersive' version='3.0'  xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation =' http://www.web3d.org/specifications/x3d-3.0.xsd '>
<Scene>
</Scene>
</X3D>
''')
f.close()
