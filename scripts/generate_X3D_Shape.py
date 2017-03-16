##X3D=group
##X3D Shape node from Appearance and  Geometry=name
##X3D_Geometry_file=file
##appearance=string <Appearance><Material></Material></Appearance>
##output_X3D_Shape_file=output file

out=open(output_X3D_Shape_file,'w')
geofile=open(X3D_Geometry_file,'r')

# no error checking, use elementtree later

out.write( '<Shape>\n' )
out.write( appearance+'\n' )
for g in geofile: out.write(g) # just write incrementally since may be large
out.write( '</Shape>\n')

geofile.close()
out.close()
