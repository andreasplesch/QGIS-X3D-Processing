'''
append x3d node to existing xml x3d scene
'''
##X3D=group
##insert X3D node into scene=name
##X3D_scene=file
##X3D_node=file
##output_X3D_scene=output file

import xml.etree.ElementTree as ET

doc = ET.parse(X3D_scene)

x3d = doc.getroot() # should be X3D element
scene = x3d.find('Scene')
scene.append(ET.parse(X3D_node).getroot())

doc.write(output_X3D_scene, 'UTF-8', True)
