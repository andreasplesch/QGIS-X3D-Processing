'''
QGIS Processing script
(c) 2017 Andreas Plesch
append x3d node to existing x3d scene in a html file
'''
##X3D=group
##insert X3D node into html=name
##X3D_html=file
##X3D_node=file
##open_in_browser=boolean False
##output_html_encoding=boolean False
##output_X3D_html=output file

import xml.etree.ElementTree as ET
#import xml.dom.minidom as DOM
import webbrowser
from PyQt4.QtCore import QUrl
from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException

doc = ET.parse(X3D_html)
#doc=DOM.parse(X3D_scene)

html = doc.getroot() # should be html element
scene = html.find('.//Scene') # first scene somewhere below
if scene is None:
    scene = html.find('.//scene')
    if scene is None:
        raise GeoAlgorithmExecutionException('Could not find a <scene> element in %s' % X3D_html)
#scene = doc.getElementsByTagName('Scene')[0]
scene.append(ET.parse(X3D_node).getroot())
#x3dNodeElement = DOM.parse(X3D_node).documentElement
#scene.appendChild(x3dNodeElement)
f = open(output_X3D_html, 'w')
encoding = 'xml'
if open_in_browser or output_html_encoding:
    encoding = 'html'
    f.write('<!DOCTYPE html>\n')
doc.write(f, 'utf-8', False, None, encoding)
#f=open(output_X3D_scene, 'w')
#doc.writexml(f, '', '  ', '', encoding='utf-8') # turns out to be not so pretty
if open_in_browser:
    url = QUrl.fromLocalFile(output_X3D_html).toString()
    webbrowser.open_new(url)
