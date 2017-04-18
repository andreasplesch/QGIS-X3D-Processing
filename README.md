# QGIS-X3D-Processing
QGIS Processing scripts, models and plugins for X3D export

## Summary
Steps to try out:
1. get a DEM (for example from ned.gov, or https://github.com/andreasplesch/QGIS-X3D-Processing/raw/master/examples/output/n35w120utmWGS84samll.tif)
2. load into qgis
3. crop and downsample to ca. 500x500 pixels, warp to longlat WGS84
4. set additional no data value in Properties - Transparency (to 0 in above DEM)
5. get all processing scripts and models from here: https://github.com/andreasplesch/QGIS-X3D-Processing/archive/master.zip
6. load into qgis
7. run raster2x3dom01 model
8. open resulting html file

## TODO

 - finalize DEM raster to GeoElevationGrid: better metadata from qgis, doc strings
 - perhaps option to enable wrap around by repeating first column after last column
 - document other scripts
 - geoOrigin option: DEF/USE, needs to be first, include optionally with empty scene and update when appending ?
 - use wiki for example processing workflow
 - add draping of other raster as texture: think about how to modularize
   - warp to crs of other raster script
   - crop/enlarge to extent of other raster script
   - save as jpg script (probably not useful): use rasterlayer.previewAsImage(full size), then Qimage.save
 - color contour option: use 1d texture and generated UVs where U is normalized elevation
 - extrude polygons from vector layer by height attribute or constant
   - need to be in projected crs, then just use first point as reference, and first point geographic coordinates for geolocation
 - GeoLOD option: use gdal tile functionality for both DEM and imagery
 - add accurate picking: done
 - passive picking: add crosshair at center and report values from there. For mobile.
 - added directional lighting: default orientation is from hillshade style azimuth and altitude
 - multidirectional option also supported
 - added svg knob to web page to interactively control directional light if available
 ...

## Examples

use PdUp/PgDown to change perspective, drag circle to hill shade

small

https://rawgit.com/andreasplesch/QGIS-X3D-Processing/master/examples/output/n35w120nedWGS84_200x200dir.html

large (takes a couple minutes to display):

https://rawgit.com/andreasplesch/QGIS-X3D-Processing/master/examples/output/grdn35w120_clipped_600x700dir.html

medium (topo30 resampled to 600x300, 100x v.e.)

https://rawgit.com/andreasplesch/QGIS-X3D-Processing/master/examples/output/topo30_600x300.html

using cobweb with pure X3D

![image](https://cloud.githubusercontent.com/assets/6171115/24529414/770ea4f4-1579-11e7-8221-1b4d24d18a6f.png)


## Documentation bits
![image](https://cloud.githubusercontent.com/assets/6171115/25078858/1877f91a-2305-11e7-8c61-b976b2b8a25d.png)

![image](https://cloud.githubusercontent.com/assets/6171115/24326416/1e4c637c-1184-11e7-8f70-bb38487f2bc0.png)

![image](https://cloud.githubusercontent.com/assets/6171115/24084642/29768dc8-0cc4-11e7-94d9-34c2ba85075a.png)

![image](https://cloud.githubusercontent.com/assets/6171115/24065920/feda64fc-0b44-11e7-9f4b-8bbc30e31c88.png)
