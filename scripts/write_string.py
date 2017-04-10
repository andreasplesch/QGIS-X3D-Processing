'''
QGIS Processing script
(c) 2017 Andreas Plesch
write input string to output file
'''
##X3D=group
##write string=name
##input_string=string the input string
##output_file=output file

f=open(output_file, 'w')
f.write(input_string)
f.close()
