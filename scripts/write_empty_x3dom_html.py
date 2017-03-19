'''
QGIS Processing script
(c) 2017 Andreas Plesch
write out a full screen style html x3dom template file
'''
##X3D=group
##write empty x3dom html=name
##output_file=output file

f=open(output_file,'w')
f.write('''<!DOCTYPE html>
<html style='width:100%; height:100%; border:0; margin:0; padding:0;'>
  
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>    
    <meta http-equiv='Content-Type' content='text/html;charset=utf-8'></meta>
    <script type='text/javascript' src='https://www.x3dom.org/release/x3dom-full.js'> </script>
    <link rel='stylesheet' type='text/css' href='https://www.x3dom.org/release/x3dom.css'/>
  </head>

<body style='width:100%; height:100%; border:0; margin:0; padding:0; background: linear-gradient(Grey 0%, White 100%);'>
    <x3d id='x3dElement' showStat='false' showLog='false' style='width:100%; height:100%; border:0' >
        <scene DEF='scene'>
        </scene>
    </x3d>
</body>
  
</html>
''')
f.close()
