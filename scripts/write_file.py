'''
QGIS Processing script
(c) 2017 Andreas Plesch
write input file to output file
'''
##X3D=group
##write file=name
##input_file=file
##output_file=file
##output_file_path=output string
##output_as_file=output file

import shutil

shutil.copy2(input_file, output_file)

output_file_path = output_file
output_as_file = output_file