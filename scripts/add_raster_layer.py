'''
QGIS Processing script
(c) 2017 Andreas Plesch
add raster layer to map
'''
##X3D=group
##add_raster=name
##input_raster=raster
##output_raster=output raster

import sys
import os
from PyQt4.QtCore import QProcess, QSettings
from qgis.gui import QgsMessageBar
from qgis.utils import iface

iface.addRasterLayer(input_raster)
output_raster=input_raster
