'''
QGIS Processing script
(c) 2017 Andreas Plesch
append x3d node to existing x3d node
'''
##X3D=group
##insert X3D node as child=name
##X3D_parent=string <Group></Group>
##X3D_node=string <DirectionalLight  />
##output_node_string=output string

import xml.etree.ElementTree as ET
#import xml.dom.minidom as DOM
#import webbrowser
#from PyQt4.QtCore import QUrl
from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException

#doc = ET.parse(X3D_html)
#doc=DOM.parse(X3D_scene)
parent = ET.fromstring(X3D_parent)

#html = doc.getroot() # should be html element
#scene = html.find('.//Scene') # first scene somewhere below
#if scene is None:
#    scene = html.find('.//scene')
#if scene is None:
#    raise GeoAlgorithmExecutionException('Could not find a <scene> element in %s' % X3D_html)

#scene = doc.getElementsByTagName('Scene')[0]
#scene.append(ET.parse(X3D_node).getroot())

parent.append(ET.fromstring(X3D_node))

#x3dNodeElement = DOM.parse(X3D_node).documentElement
#scene.appendChild(x3dNodeElement)
method = 'xml'
output_node_string = ET.tostring(parent, 'utf-8', method)
#print(output_node_string)
#if open_in_browser or output_html_encoding: encoding = 'html'
#doc.write(output_X3D_html, 'utf-8', False, None, encoding)
#f=open(output_X3D_scene, 'w')
#doc.writexml(f, '', '  ', '', encoding='utf-8') # turns out to be not so pretty
#if open_in_browser:
 #   url = QUrl.fromLocalFile(output_X3D_html).toString()
  #  webbrowser.open_new(url)