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
    <script type="text/javascript" src=
    'https://cdn.rawgit.com/andreasplesch/e2cd02fd30ff74670e00758e46c1679c/raw/08cad8f391fe6242fe7e44373df0d9dead00d8b6/x3dom_HDpick.user.js'
    > </script>
    <link rel='stylesheet' type='text/css' href='https://www.x3dom.org/release/x3dom.css'/>
    <style>
        div#hud {
            position:  fixed;
            padding: 10px;
            width: 25%;
            top: 0;
            right: 0;
            z-index: 9999;
            background: white;
            opacity: 0.5;
            /* text-shadow: 3px 3px 2px black; */
            /* box-shadow: -5px 5px 4px 0px black; */
        }
    </style>
  </head>

<body style='width:100%; height:100%; border:0; margin:0; padding:0; background: linear-gradient(Grey 0%, White 100%);'>
<div id='hud'> HUD area </div>
    <x3d id='x3dElement' showStat='false' showLog='false' style='width:100%; height:100%; border:0' >
        <scene DEF='scene'>
        </scene>
    </x3d>
    <script>
        document.onload = function () {
            //listen to mouse
            var scene = document.querySelector('scene');
            scene.addEventListener('mousemove', updatePointing, false);//improved but slow picking with HD picker addon
        }
        function updatePointing (event) {
            //update HUD
            var hud = document.querySelector('#hud');
            var gc = x3dom.fields.MFVec3f.parse(event.hitPnt.toString());
            var gd = x3dom.nodeTypes.GeoCoordinate.prototype.GCtoGD(['GC','WE'], gc)[0];
            var veNode = event.hitObject.querySelector('[yscale]'); // any child object with yscale attribute
            var ve = veNode ? 1.0 * veNode.yscale : 1.0 ;
            hud.textContent = "long.: "+gd.x.toFixed(3)+"° lat.: "+gd.y.toFixed(3)+"° height: "+(gd.z/ve).toFixed(1)+"m";
        }
    </script>
</body>
</html>
''')
f.close()
