# 11-classwork: Mapping in QGIS

### General notes about mapping
* Custom: Mapbox GL, Leaflet
* Hosted/wizards: google maps, CARTO, mapbox, ESRI
* Maps are all about layers: image base, elevation, hydrography (water), boundaries, land use, roads
* Earth = an ellipsoid, the datum tells you where the ellipsoid goes

### QGIS notes
* CRS options: 
    * NAD-83 is best for North America
    * WGS-84 is best for the world
* Once QGIS is open, you can just double click to open shapefiles
* In layer properties, select color scale, variable, (symbol type, if not polygons) and select “Classify” to apply the range
    * Can alter intervals in the “Mode” menu - Equal count is same number of counts in each one & natural breaks uses math to determine best places to break
* To count the number of points in each layer to make a choropleth
    * Vector > Analysis > Count vectors in polygon > Select the variable with the points — Note that this creates a new layer (it does not edit the existing layer)
    * Note: Count field name here has a max length
