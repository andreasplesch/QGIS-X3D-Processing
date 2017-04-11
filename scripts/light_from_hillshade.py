'''
QGIS Processing script
(c) 2017 Andreas Plesch
constructs directional light from azimuth and altitude
'''
##X3D=group
##light from hillshade=name
##azimuth=number 315
##altitude=number 45
##multidirectional=boolean False
##output_X3D_light=output string

out ='<Transform rotation="0 1 0 %s">\n’ % azimuth
out+='    <Transform rotation="1 0 0 %s">\n’ % altitude
out+='        <DirectionalLight />\n'
out+='    </Transform>\n'
out+='</Transform>\n'

output_X3D_light=out
