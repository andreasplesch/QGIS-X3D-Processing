'''QGIS Processing script
(c) 2017 Andreas Plesch
saves raster layer as flipped and scaled image
to be used as texture
'''
##X3D=group
##save as texture file=name
##input_raster=raster
##image_format=selection jpg;png;tiff
##output_folder=folder
##output_path=output string
##output_filename=output string
##output_isAvailable=output string

import math
from PyQt4.QtCore import QSize, QDir, QFileInfo
from qgis.utils import iface

PXMAX = 4096
image_formats = {
    0: 'jpg',
    1: 'png',
    2: 'tif'
}
output_path = 'notUsed'
output_filename = 'notUsed'
output_isAvailable = 'False'

if image_format is None: image_format = 0

def npow2(n):
    return min(2**(math.ceil(math.log(n,2))), PXMAX)

#image = iface.mainWindow().windowIcon().pixmap(32,32)
#name = 'default'

if input_raster is not None:
    r = processing.getObject(input_raster)
    rw = r.width()
    rh = r.height()
    size = QSize(rw,rh)
    size2 = QSize(npow2(rw),npow2(rh))
    image = r.previewAsImage(size).mirrored(vertical=True).scaled(size2)
    name = r.name()
    output_filename = name+'_tex.'+image_formats[image_format]
    qInfo = QFileInfo(output_folder)
    qfolder = qInfo.dir()
    if qInfo.isDir(): qfolder = QDir(output_folder)
    output_path = qfolder.absoluteFilePath(output_filename)
    image.save(output_path)
    output_isAvailable = 'True'

print(output_filename, output_path, image_format)