'''
QGIS Processing script
(c) 2017 Andreas Plesch
serve html file and show in browser
'''
##X3D=group
##serve_and_open_html=name
##input_html=file
##server_port=number 8000
##open_in_browser=boolean False
##html_file_name=output string

import shutil
import webbrowser
from PyQt4.QtCore import QUrl, QFileInfo

port = int(server_port)

if open_in_browser:
    html = QFileInfo(input_html)
    root_folder = html.canonicalPath()
    # kills running web server if necessary
    processing.runalg('script:launchwebserver', root_folder, port)
    #url = QUrl.fromLocalFile(output_file).toString()
    url = 'http://localhost:%s/%s' % (port, html.fileName())
    webbrowser.open_new(url)
    
html_file_name = html.fileName()