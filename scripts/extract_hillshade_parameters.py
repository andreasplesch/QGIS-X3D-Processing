'''
QGIS Processing script
(c) 2017 Andreas Plesch
extracts parameters used for hillshade rendering
custom values if not active renderer
'''
##X3D=group
##hillshade parameters=name
##input_raster=raster
##use_custom_parameters=boolean False
##custom_azimuth=number 315
##custom_altitude=number 45
##custom_zFactor=number 1
##custom_multidirectional=boolean False
##out_azimuth=output number
##out_altitude=output number
##out_zFactor=output number
##out_multidirectional=output number

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
