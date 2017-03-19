'''
append x3d node to existing xml x3d scene
'''
##X3D=group
##insert X3D node into html=name
##X3D_html=file
##X3D_node=file
##output_X3D_html=output file
##open_in_browser=boolean False

import xml.etree.ElementTree as ET
#import xml.dom.minidom as DOM
import webbrowser
from PyQt4.QtCore import QUrl

doc = ET.parse(X3D_html)
#doc=DOM.parse(X3D_scene)

html = doc.getroot() # should be html element
scene = html.find('.//Scene') # first scene somewhere below
if scene is None:
    scene = html.find('.//scene')
if scene is None:
    print('raise exception here')
#scene = doc.getElementsByTagName('Scene')[0]
scene.append(ET.parse(X3D_node).getroot())
#x3dNodeElement = DOM.parse(X3D_node).documentElement
#scene.appendChild(x3dNodeElement)

doc.write(output_X3D_html, 'utf-8', False, None, 'xml')
#f=open(output_X3D_scene, 'w')
#doc.writexml(f, '', '  ', '', encoding='utf-8') # turns out to be not so pretty
if open_in_browser:
    url = QUrl.fromLocalFile(output_X3D_html).toString()
    webbrowser.open_new(url)