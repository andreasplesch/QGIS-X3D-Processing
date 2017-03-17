'''
append x3d node to existing xml x3d scene
'''
##X3D=group
##insert X3D node into scene=name
##X3D_scene=file
##X3D_node=file
##output_X3D_scene=output file

import xml.etree.ElementTree as ET
#import xml.dom.minidom as DOM

doc = ET.parse(X3D_scene)
#doc=DOM.parse(X3D_scene)

x3d = doc.getroot() # should be X3D element
scene = x3d.find('Scene')
#scene = doc.getElementsByTagName('Scene')[0]
scene.append(ET.parse(X3D_node).getroot())
#x3dNodeElement = DOM.parse(X3D_node).documentElement
#scene.appendChild(x3dNodeElement)

doc.write(output_X3D_scene, 'utf-8', True)
#f=open(output_X3D_scene, 'w')
#doc.writexml(f, '', '  ', '', encoding='utf-8') # turns out to be not so pretty
