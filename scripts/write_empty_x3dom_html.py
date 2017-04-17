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
        #x3dElement {
            width: 100%;
            height: 100%;
            border: 0;
        }
        div#lightcontrol {
            position:  fixed;
            padding: 0px;
            width: 100px;
            height: 100px;
            top: 10px;
            left: 10px;
            z-index: 9999;
            //background: white;
            //opacity: 0.5;
        }
        #lightdot:hover {
            fill: red;
        }
    </style>
  </head>

<body style='width:100%; height:100%; border:0; margin:0; padding:0; background: linear-gradient(Grey 0%, White 100%);'>
    <div id='hud'> HUD area </div>
    <div id='lightcontrol'>
        <svg version="1.1"
            baseProfile="full"
            width="100px" height="100px"
            >
            <circle cx="50%" cy="50%" r="50" stroke="black" stroke-width="2" fill="white" opacity="0.5" />
            <circle cx="50%" cy="50%" r="2" stroke="black" stroke-width="2" fill="transparent" />
            <text id='lighttext' x="50%" y="25%" font-size="12" text-anchor="middle" >0 90</text>
            <circle id="lightdot" cx="50%" cy="50%" r="10" fill="black" onmousemove="updateLight(evt)"/>
        </svg>
    </div>
    <X3D id='x3dElement' showStat='false' showLog='false'>
        <Scene DEF='scene'>
            <NavigationInfo headlight='false'></NavigationInfo>
        </Scene>
    </X3D>
    <script>
        document.onload = function () {
            var lightRect = document.querySelector('#lightcontrol').getBoundingClientRect();
            var lightText = document.querySelector('#lighttext');
            var r2d = 180/Math.PI;
            updateLight = function (e) {
                if (e.buttons !== 1) {return}
                var c = e.currentTarget;
                c.setAttribute('cx', e.layerX);
                c.setAttribute('cy', e.layerY);
                var x = e.layerX - lightRect.width/2;
                var y = e.layerY - lightRect.height/2;
                var az = (Math.atan2(y, x) * r2d + 90) % 360;
                var al = 90 - Math.hypot(x/lightRect.width, y/lightRect.height) * 180;
                lightText.textContent=az.toFixed(0)+" "+al.toFixed(0);
                var dirLight = scene.querySelector('DirectionalLight');
                if (dirLight) {
                    var alRot = dirLight.parentNode;
                    alRot.setAttribute('rotation', '1 0 0 ' + (-al / r2d));
                    var azRot = alRot.parentNode;
                    azRot.setAttribute('rotation', '0 1 0 ' + (180 - az)/r2d);
                }
            }
            // listen to mouse
            var scene = document.querySelector('scene');
            var hud = document.querySelector('#hud');
            scene.addEventListener('mousemove', updatePointing, false);//improved but slow picking with HD picker addon
            // switch headlight on if no other lights
            var lights = scene.querySelector('PointLight, DirectionalLight, SpotLight');
            if (!lights) {
                var runtime = document.querySelector('X3D').runtime ;
                var navInfo = runtime.getActiveBindable('NavigationInfo') ;
                navInfo.setAttribute('headlight', true);}
            function updatePointing (event) {
                //update HUD
                var gc = x3dom.fields.MFVec3f.parse(event.hitPnt.toString());
                var gd = x3dom.nodeTypes.GeoCoordinate.prototype.GCtoGD(['GC','WE'], gc)[0];
                var veNode = event.hitObject.querySelector('[yscale]'); // any child object with yscale attribute
                var ve = veNode ? 1.0 * veNode.yscale : 1.0 ;
                hud.textContent = "long.: "+gd.x.toFixed(3)+"° lat.: "+gd.y.toFixed(3)+"° height: "+(gd.z/ve).toFixed(1)+"m";
            }
        }
    </script>
</body>
</html>
''')
f.close()
