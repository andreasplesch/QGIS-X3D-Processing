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
            padding: 5px;
            width: 210px;
            height: 210px;
            top: 0px;
            left: 0px;
            z-index: 9999;
            background: white;
            opacity: 0.7;
        }
        #lightsvg {
            width: 100%;
            height: 100%;
        }
        #lightdot:hover {
            fill: red;
            cursor: move;
        }
        #lightcircle:hover {
            cursor: crosshair;
        }
        .lighttext::selection {
            background: none;
        }
        .lighttext {
            font-size: 14px;
        }
    </style>
  </head>

<body style='width:100%; height:100%; border:0; margin:0; padding:0; background: linear-gradient(Grey 0%, White 100%);'>
    <div id='hud'> HUD area </div>
    <div id="lightcontrol">
        <svg id="lightsvg" baseprofile="full" version="1.1" >
            <circle id="lightcircle" cx="50%" cy="50%" fill="white" opacity="0.5" r="100" stroke="black" stroke-width="2"></circle>
            <circle cx="50%" cy="50%" fill="transparent" r="2" stroke="black" stroke-width="2"></circle>
            <text id="azimuthtext"  class="lighttext" text-anchor="start" x="0" y="12">0°</text>
            <text id="altitudetext"  class="lighttext" text-anchor="end" x="100%" y="12">90°</text>
            <circle cx="50%" cy="50%" fill="black" id="lightdot" r="10" ></circle>
        </svg>
    </div>
    <X3D id='x3dElement' showStat='false' showLog='false'>
        <Scene DEF='scene'>
            <NavigationInfo headlight='false'></NavigationInfo>
        </Scene>
    </X3D>
    <script type="text/javascript">
        //<![CDATA[
        document.onload = function () {
          
            // light control
            var lightCircle = document.querySelector('#lightcircle');
            var lightRect = lightCircle.getBoundingClientRect();
            var lightCenterSVG = {"x":lightCircle.cx.baseVal.value, "y":lightCircle.cy.baseVal.value};
            var lightCenter = {"x":(lightRect.right + lightRect.left) / 2, "y":(lightRect.top + lightRect.bottom) / 2};
            var azimuthText = document.querySelector('#azimuthtext');
            var altitudeText = document.querySelector('#altitudetext');
            var lightDot =  document.querySelector('#lightdot');
            
            var r2d = 180/Math.PI;
          
            lightCircle.addEventListener('touchmove', updateLight, false);
            lightDot.addEventListener('touchmove', updateLight, false);
            lightCircle.addEventListener('mousemove', updateLight, false);
            lightDot.addEventListener('mousemove', updateLight, false);
            lightCircle.addEventListener('mousedown', updateLight, false);
          
            function updateLight (e) {
                if ((e.buttons !== 1) && (e.type !== 'touchmove')) {return}
                e.stopPropagation();
                //var c = e.currentTarget;
                var clientX = e.clientX || e.changedTouches[0].clientX;
                var clientY = e.clientY || e.changedTouches[0].clientY;
                
                var x = clientX - lightCenter.x;
                var y = clientY - lightCenter.y;
                var cx = lightCenterSVG.x + x ;
                var cy = lightCenterSVG.y + y ;
                lightDot.setAttribute('cx', cx);
                lightDot.setAttribute('cy', cy);
                var az = (Math.atan2(y, x) * r2d + 90 + 360) % 360;
                x /= lightRect.width ;
                y /= lightRect.height ;
                var al = 90 - Math.sqrt(x*x + y*y) * 180; // no Math.hypot in IE
                azimuthText.textContent=("00"+az.toFixed(0)).slice(-3)+"°";
                altitudeText.textContent=("0"+al.toFixed(0)).slice(-2)+"°";
                var dirLight = scene.querySelector('DirectionalLight');
                if (dirLight) {
                    var alRot = dirLight.parentNode;
                    alRot.setAttribute('rotation', '1 0 0 ' + (-al / r2d));
                    var azRot = alRot.parentNode;
                    azRot.setAttribute('rotation', '0 1 0 ' + (180 - az) / r2d);
                }
            }
            // picking, lights
            var x3dElement = document.querySelector('X3D');
            var scene = x3dElement.querySelector('scene');
            var hud = document.querySelector('#hud');
            
            // switch headlight on if no other lights
            var lights = scene.querySelector('PointLight, DirectionalLight, SpotLight');
            var runtime = x3dElement.runtime ;
            var navInfo = runtime.getActiveBindable('NavigationInfo') ;
            if (!lights) {
                navInfo.setAttribute('headlight', true);
            }
            
            x3dElement.addEventListener('keypress', toggleHeadlight, false);
            
            function toggleHeadlight (event) {
                if (event.charCode !== 120) {return;} //'x'
                var hl = navInfo.getFieldValue('headlight');
                navInfo.setFieldValue('headlight', !hl);
            }
            
            scene.addEventListener('mousemove', updatePointing, false);//improved but slow picking with HD picker addon
            
            function updatePointing (event) {
                //update HUD
                var gc = x3dom.fields.MFVec3f.parse(event.hitPnt.toString());
                var gd = x3dom.nodeTypes.GeoCoordinate.prototype.GCtoGD(['GC','WE'], gc)[0];
                var veNode = event.hitObject.querySelector('[yscale]'); // any child object with yscale attribute
                var ve = veNode ? 1.0 * veNode.yscale : 1.0 ;
                hud.textContent = "long.: "+gd.x.toFixed(3)+"° lat.: "+gd.y.toFixed(3)+"° height: "+(gd.z/ve).toFixed(1)+"m";
            }
        }
        //]]>
    </script>
</body>
</html>
''')
f.close()
