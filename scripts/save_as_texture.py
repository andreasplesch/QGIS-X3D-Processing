'''QGIS Processing script
(c) 2017 Andreas Plesch
saves raster layer as flipped and scaled image
to be used as texture
'''
##X3D=group
##save_as_texture_file=name
##input_raster=raster
##image_format=selection jpg;png;tiff
##output_folder=folder
##output_filename=output string

import math
from PyQt4.QtCore import QSize, QDir

PXMAX = 4096
image_formats = {
    0: 'jpg',
    1: 'png',
    2: 'tif'
}

if image_format is None: image_format = 0

def npow2(n):
    return min(2**(math.ceil(math.log(n,2))), PXMAX)

r = processing.getObject(input_raster)
rw = r.width()
rh = r.height()
size = QSize(rw,rh)
size2 = QSize(npow2(rw),npow2(rh))
image = r.previewAsImage(size).mirrored(vertical=True).scaled(size2)
output_filename = QDir(output_folder).absoluteFilePath(r.name()+'_tex.'+image_formats[image_format])
image.save(output_filename)
#print(output_filename,image_format)