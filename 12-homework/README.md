# 12-homework: QGIS

Hexbins map on art galleries
* Tutorials: https://jonathansoma.com/lede/foundations-2018/qgis/grid/ and https://youtu.be/wyVCdC4l77k 
* Data on art galleries from [NYC Open Data](https://data.cityofnewyork.us/Recreation/New-York-City-Art-Galleries/tgyc-r5jh)
* NYC Borough Boundaries (Clipped to Shoreline) shapefile from [NYC Planning](https://www1.nyc.gov/site/planning/data-maps/open-data/districts-download-metadata.page)
* Borough names from NYC DCP Mapping Portal via [ArcGIS Hub](https://hub.arcgis.com/datasets/DCP::nyc-borough-boundary/about)

Map of tornado tracks
* Data loaded in from Soma's [tutorial](https://gist.github.com/jsoma/807c07ad59064b7fef96c8d561834e2d)
    * Width and color adjusted based on "mag" variable (magnitude)
* Blending mode - Layer: Addition, Feature: Screen
* Earth topography loaded from [Natural Earth data](https://www.naturalearthdata.com/downloads/10m-raster-data/10m-shaded-relief/)
    * File clipped to US geography with Raster > Clip Raster by Mask Layer. Also lowered brightness in properties

Choropleth map of building age
* Shapefile from [NYC Planning](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page)
    * Graduated colors based on "YearBuilt", stroke: No Pen
* Neighborhood names from [NYC Open Data](https://data.cityofnewyork.us/City-Government/Neighborhood-Names-GIS/99bc-9p23/data)

More maps that I didn't get around to completing are [here](https://gist.github.com/jsoma/807c07ad59064b7fef96c8d561834e2d)
