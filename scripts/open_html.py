'''
QGIS Processing script
(c) 2017 Andreas Plesch
open html in browser
'''
##X3D=group
##open html in default browser=name
##html_file=file
##open_in_browser=boolean False

import webbrowser
from PyQt4.QtCore import QUrl

if open_in_browser:
    url = QUrl.fromLocalFile(html_file).toString()
    webbrowser.open_new(url)
