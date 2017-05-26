'''
QGIS Processing script
(c) 2017 Andreas Plesch
write input file to output file and show in browser
'''
##X3D=group
##write file=name
##input_file=file
##output_file=file
##open_in_browser=boolean False
##output_file_as_string=output string

import shutil
import webbrowser
from PyQt4.QtCore import QUrl, QFileInfo

shutil.copy2(input_file, output_file)

if open_in_browser:
    output = QFileInfo(output_file)
    root_folder = output.canonicalPath()
    processing.runalg('script:launchwebserver', root_folder, 8000)
    #url = QUrl.fromLocalFile(output_file).toString()
    url = 'http://localhost:8000/%s' % output.fileName()
    webbrowser.open_new(url)
    
output_file_as_string = output_file