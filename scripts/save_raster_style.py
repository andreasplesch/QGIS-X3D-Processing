'''
QGIS Processing script
(c) 2017 Andreas Plesch
save style in qml file
'''
##X3D=group
##save_raster_style=name
##input_raster=raster
##style_file=output file

import shutil
from PyQt4.QtCore import QFile, QFileInfo, QDir

#saveNamedStyle always writes to .qml
fileInfo = QFileInfo(style_file)
style_file = fileInfo.path() + QDir.separator() + fileInfo.completeBaseName() + ".qml"

file=QFile(style_file)
#touch, create since saveStyle only writes file if it exists
file.open(QFile.ReadWrite)
file.close()

r = processing.getObject(input_raster)
print(r.saveNamedStyle(style_file))
#saveNamedStyle always writes to .qml
#copy back
#fileInfo = QFileInfo(style_file)
#style_file = fileInfo.path() + QDir.separator() + fileInfo.completeBaseName() + ".qml"
#shutil.copy(qml, style_file)


