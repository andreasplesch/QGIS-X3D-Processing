# QGIS-X3D-Processing
QGIS Processing scripts, models and plugins for X3D export

## Summary
Steps to try out:
1. get a DEM (for example from ned.gov)
2. load into qgis
3. crop and downsample to ca. 500x500 pixels
4. get all processing scripts and models from here
5. load into qgis
6. run raster2x3dom model
7. open resulting html file

## TODO

 - finalize DEM raster to GeoElevationGrid: better metadata from qgis, doc strings
 - document other scripts
 - use wiki for example processing
 - add draping of other raster as texture: think about how to modularize
 -- warp to crs of other raster script
 -- crop/enlarge to extent of other raster script
 -- save as jpg script (probably not useful)
 - color contour option: use 1d texture and generated UVs where U is normalized elevation
 ...

## Examples

small

https://rawgit.com/andreasplesch/QGIS-X3D-Processing/master/examples/output/n35w120n_ned_small.html

large (takes a couple minutes to display):

https://rawgit.com/andreasplesch/QGIS-X3D-Processing/master/examples/output/x3dom2.html

## Documentation bits

![image](https://cloud.githubusercontent.com/assets/6171115/24065920/feda64fc-0b44-11e7-9f4b-8bbc30e31c88.png)
