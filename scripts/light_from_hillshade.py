'''
QGIS Processing script
(c) 2017 Andreas Plesch
constructs directional light from azimuth and altitude
'''
##X3D=group
##light from hiillshade=name
##azimuth=number 315
##altitude=number 45
##multidirectional=boolean False
##output_X3D_light=output string

import PyQt4.QtXml as qxml

dem = processing.getObject(input_raster)
r=dem.renderer()

out_azimuth=custom_azimuth
out_altitude=custom_altitude
out_zFactor=custom_zFactor
out_multidirectional=float(custom_multidirectional)

if r.type() == u'hillshade' and not(use_custom_parameters):
    doc = qxml.QDomDocument()
    lElement=doc.createElement('rasterlayer') #some required parent tag
    r.writeXML(doc, lElement)
    rElement=lElement.firstChild().toElement()
    out_azimuth = float(rElement.attribute('azimuth'))
    out_altitude = float(rElement.attribute('angle'))
    out_zFactor = float(rElement.attribute('zfactor'))
    out_multidirectional= float(rElement.attribute('multidirection'))
