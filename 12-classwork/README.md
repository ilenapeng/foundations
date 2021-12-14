# 12-classwork: QGIS

### Animated map
* Properties > Temporal Control > Check Dynamic Temporal Control > Configuration: Single Field with Date/Time > Field: time (our variable) > Event duration: 1
* Go to top bar: View > Panels > Temporal Controller > Click the play button on the far right of the menu in the top left
* Change “Steps” to how often you want QGIS’ animation to change (For the one in class, which was the span of a month, we used 1 day)
* Click the settings icon in the top right to set it to X rates per second to have it move faster (default is 1 rate per second)
* View > Decoration > Title Labels > Check Enable Title Label > input [%format_date(@map_start_time, 'yyyy-MM-dd')%] in the text field 
* Click the floppy disk icon to save > upload files to https://ezgif.com/ to create a GIF

### 3D map
* A geotiff image can be placed on a map
* Drag in n37_w120… file (place underneath) 11565_2019… file
* View > New 3D map view > Wrench > Configure > select DEM in the dropdown menu (Digital Elevation Map, is a raster layer) > Select the variable that contains the DEM
* Press down "Shift" to adjust the map's perspective

### US map with joins
* After uploading state tiles, add in state data in "Joining Data" folder > Select “No geometry (attribute only table)”
* Open properties on US state > Select “Joins” > Select “Plus” button > Join “State” column to “NAME” column
* Adjust properties like normal
* Add in wafflehouses data from Week 11
* Vector > Analysis Tools > Count Points in Polygon
* To add average score for every waffle house: Join Attributes By Location > Base layer: Count, Join layer: waffle points > Check "contains" and "within" in the predicates > Summarize the “Score” variable by the mean
* On that new joined layer > Join attributes by location > Select ‘contains and within’ > Select ‘Take attributes of the first matching feature only’
* Then on that joined layer of points > Properties > Categorized colors by Name
* Can also open attribute table > Open Field Calculator (Ctrl-I) > Scroll to “Fields and Values” and double click the column you want

### OpenStreetMap
* Plugins > Manage and Install Plugins > Install “Quick OSM”
* To use OSM:
    * Click OSM icon > In: “Morningside Heights, New York City” > Run query
    * Browser > XYZ Tiles > Drag “OpenStreetMap” into your “Layers” > Zoom to wherever you want > In the dropdown menu that default says “In,” select “Canvas Extent” > Run query
