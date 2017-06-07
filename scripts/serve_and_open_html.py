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
html = QFileInfo(input_html)
html_file_name = html.fileName()

if open_in_browser:
    root_folder = html.canonicalPath()
    # kills running web server if necessary
    processing.runalg('script:launchwebserver', root_folder, port)
    #url = QUrl.fromLocalFile(output_file).toString()
    #deal with spaces and such
    url = QUrl(u'http://localhost:%s/%s' % (port, html_file_name))
    #perhaps warn if not ending in html
    webbrowser.open_new(url.toString())

