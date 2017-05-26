# coding: utf-8
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
<html style="width:100%; height:100%; border:0; margin:0; padding:0;">
  
  <head>
    <meta content="IE=edge" http-equiv="X-UA-Compatible" />    
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type" />
    <script src="https://www.x3dom.org/release/x3dom-full.js" type="text/javascript"></script>
    <script src="https://cdn.rawgit.com/andreasplesch/e2cd02fd30ff74670e00758e46c1679c/raw/08cad8f391fe6242fe7e44373df0d9dead00d8b6/x3dom_HDpick.user.js" type="text/javascript"></script>
    <script src="https://cdn.rawgit.com/mourner/suncalc/master/suncalc.js" type="text/javascript"></script>
    <link href="https://www.x3dom.org/release/x3dom.css" rel="stylesheet" type="text/css"/>
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
        #timecontrol {
            position: fixed;
            margin-left: 30%;
            margin-right: 30%;
            width: 40%;
            padding: 10px;
            z-index: 9999;
            background: rgba(255, 255, 255, 0.5);
        }
        #timelabel {
            display: block;
            text-align: center;
            font-size: 14px;
        }
        #timeslider {
            width: 100%;
        }
        .timeZoomButton {
          font-size: 20px;
        }
        .timeZoomButton:hover {
          cursor: crosshair;
          background: red;
        }
        #timeMax {
          float: right;
        }
    </style>
  </head>

<body style="width:100%; height:100%; border:0; margin:0; padding:0; background: linear-gradient(Grey 0%, White 100%);">
  <div id="hud"> HUD area </div>
  <div title="control lighting by dragging dot, toggle with 'z'" id="lightcontrol">
      <svg id="lightsvg" baseprofile="full" version="1.1" >
          <circle id="lightcircle" cx="50%" cy="50%" r="100" fill="none" stroke="black" stroke-width="2"
                  pointer-events="visible" ></circle>
          <line x1="50%" x2="50%" y1="5%" y2="15%" stroke="black" stroke-width="2"/> 
          <circle cx="50%" cy="50%" fill="transparent" r="2" stroke="black" stroke-width="2"></circle>
          <text id="azimuthtext"  class="lighttext" text-anchor="start" x="0" y="12">000°</text>
          <text id="altitudetext"  class="lighttext" text-anchor="end" x="100%" y="12">90°</text>
          <circle cx="50%" cy="50%" fill="black" id="lightdot" r="10"></circle>
      </svg>
  </div>
  <div title="toggle with 'z'" id="timecontrol">
    <button title="zoom into time period" id="timeZoomIn" class="timeZoomButton"> + </button>
    <button title="recenter time period" id="timeRecenter" class="timeZoomButton"> = </button>
    <button title="zoom out of time period" id="timeZoomOut" class="timeZoomButton"> - </button>
    <label id="timelabel" for="timeslider">pick a time </label>
    <input id="timeslider" type="range" min="0" max="1000000" step="1"></input>
    <span id="timeMin">0</span>
    <span id="timeMax">0</span>
  </div>
    <X3D id='x3dElement' showStat='false' showLog='false'>
        <Scene DEF='scene'>
            <NavigationInfo headlight='false'></NavigationInfo>
        </Scene>
    </X3D>
    <script type="text/javascript">
        //<![CDATA[
        document.onload = function () {
            
            var degGlyph = "°";
            var x3dElement = document.querySelector('X3D');
            var scene = x3dElement.querySelector('scene');
            
            var timeControl = document.querySelector('#timecontrol');
            var lightControl = document.querySelector('#lightcontrol');
            
            var controlsDisplay = 3;
            // toggle controls
            x3dElement.addEventListener('keypress', toggleControls, false);
          
            function toggleControls (e) {
              if (e.charCode !== 122) {return;} //'z'
              
              var timeControlDisplay = 'none';
              var lightControlDisplay = 'none';
              
              controlsDisplay = ++controlsDisplay % 4 ;
              if (controlsDisplay & 1) {
                lightControlDisplay = 'block';
              }
              if (controlsDisplay & 2) {
                timeControlDisplay = 'block';
              }
              
              timeControl.style.display = timeControlDisplay;
              lightControl.style.display = lightControlDisplay;
            }
          
              
            // time control
            var timeLabel = document.querySelector('#timelabel');
            var timeSlider = document.querySelector('#timeslider');
            var timeMin = document.querySelector('#timeMin');
            var timeMax = document.querySelector('#timeMax');
            var timeZoomIn = document.querySelector('#timeZoomIn');
            var timeZoomOut = document.querySelector('#timeZoomOut');
            var timeRecenter = document.querySelector('#timeRecenter');
            var time = new Date();
            var timeCenter = Date.now();
            var timeRange = 7 * 24 * 3600 * 1000;
            
            function updateTimeRange () {
              timeSlider.min = timeCenter - timeRange/2;
              timeSlider.max = timeCenter + timeRange/2;
              timeMin.textContent = new Date(1.0 * timeSlider.min).toDateString();
              timeMax.textContent = new Date(1.0 * timeSlider.max).toDateString();
            };
          
            updateTimeRange ();
            timeSlider.value = timeCenter;
            
            timeZoomIn.addEventListener('click', zoomInTimeRange, false); 
            timeZoomOut.addEventListener('click', zoomOutTimeRange, false); 
            timeRecenter.addEventListener('click', recenterTimeRange, false); 
            
            function recenterTimeRange (e) {
              timeCenter = timeSlider.valueAsNumber;
              updateTimeRange();
            }
            function zoomInTimeRange (e) {
              timeRange /= 2;
              updateTimeRange();
            }
            function zoomOutTimeRange (e) {
              timeRange *= 2;
              updateTimeRange();
            }    
        
            var geoCenter = document.querySelector('GeoViewpoint').getAttribute("centerOfRotation").split(" ");
            
            var r2d = 180/Math.PI;
          
            timeSlider.addEventListener('input', updateTime, false);
            timeSlider.addEventListener('change', updateTime, false); //for IE
            
            function updateTime (e) {
              time.setTime(e.target.valueAsNumber);
              timeLabel.textContent = time.toDateString();
              timeLabel.textContent += ", " + padZeroes(time.getHours(),2) + ":" + padZeroes(time.getMinutes(), 2) ;
              timeLabel.textContent += " (UTC-" + time.getTimezoneOffset()/60 + "h)" ;
              
              var sunPosition = SunCalc.getPosition(time, 1.0 * geoCenter[0], 1.0 * geoCenter[1]);
              var al = sunPosition.altitude * r2d; 
              var az = (sunPosition.azimuth * r2d + 180 ) % 360;
              
              updateLightDot(az, al);
              
              updateDirLight(az, al);
            }
          
            function updateLightDot(az, al) {
              var r = (90 - al) / 180; //0.5 * (90 - al) / 90 ;
              var a = (az - 90) / r2d;
              var x = r * Math.cos(a) * lightRect.width;
              var y = r * Math.sin(a) * lightRect.height;
              
              var cx = lightCenterSVG.x + x ;
              var cy = lightCenterSVG.y + y ;
              lightDot.setAttribute('cx', cx);
              lightDot.setAttribute('cy', cy);
            }
          
            function updateDirLight(az, al) {
              azimuthText.textContent = padZeroes(az, 3) + degGlyph;
              altitudeText.textContent = padZeroes(al, 2) + degGlyph;
                
              if (dirLight) {
                var alRot = dirLight.parentNode;
                alRot.setAttribute('rotation', '1 0 0 ' + (-al / r2d));
                var azRot = alRot.parentNode;
                azRot.setAttribute('rotation', '0 1 0 ' + (180 - az) / r2d);
              }
            }
          
            function padZeroes (number, digits) {
              return ("00000000" + number.toFixed(0)).slice(-digits);
            }
          
            // light control
            var lightCircle = document.querySelector('#lightcircle');
            var lightRect = lightCircle.getBoundingClientRect();
            var lightCenterSVG = {"x":lightCircle.cx.baseVal.value, "y":lightCircle.cy.baseVal.value};
            var lightCenter = {"x":(lightRect.right + lightRect.left) / 2, "y":(lightRect.top + lightRect.bottom) / 2};
            var azimuthText = document.querySelector('#azimuthtext');
            var altitudeText = document.querySelector('#altitudetext');
            var lightDot =  document.querySelector('#lightdot');
            
            // init control
            var dirLight = scene.querySelector('DirectionalLight');
            if (dirLight) {
              var alRot = dirLight.parentNode;
              var al = -alRot.getAttribute('rotation').split(' ')[3] * r2d;
              var azRot = alRot.parentNode;
              var az = (180 - azRot.getAttribute('rotation').split(' ')[3] * r2d + 360) % 360;
              updateDirLight(az, al);
              updateLightDot(az, al);
            }
            
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
                updateDirLight(az, al);
            }
            // picking, lights
            var hud = document.querySelector('#hud');
            
          // switch headlight on if no other lights
            var lights = scene.querySelector('PointLight, DirectionalLight, SpotLight');
            var runtime = x3dElement.runtime ;
            var navInfo = runtime.getActiveBindable('NavigationInfo') ;
            if (!lights) {
                navInfo.setAttribute('headlight', true);
            }
            
            scene.addEventListener('mousemove', updatePointing, false);//improved but slow picking with HD picker addon
            
            x3dElement.addEventListener('keypress', toggleHeadlight, false);
            
            function toggleHeadlight (event) {
                if (event.charCode !== 120) {return;} //'x'
                var hl = navInfo.getFieldValue('headlight');
                navInfo.setFieldValue('headlight', !hl);
            }
          
            function updatePointing (event) {
                //update HUD
                var gc = x3dom.fields.MFVec3f.parse(event.hitPnt.toString());
                var gd = x3dom.nodeTypes.GeoCoordinate.prototype.GCtoGD(['GC','WE'], gc)[0];
                var veNode = event.hitObject.querySelector('[yscale]'); // any child object with yscale attribute
                var ve = veNode ? 1.0 * veNode.yscale : 1.0 ;
                hud.textContent = "long.: "+gd.x.toFixed(3)+degGlyph+" lat.: "+gd.y.toFixed(3)+degGlyph+" height: "+(gd.z/ve).toFixed(1)+"m";
            }
        }
        //]]>
    </script>
</body>
</html>
''')
f.close()
