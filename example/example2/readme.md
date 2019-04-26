# Creating GeoJSON to Vector Tiles with Tippecanoe then serving them with a local Python http server


Step 1: 


# Install Tippecanoe

https://github.com/mapbox/tippecanoe

You will likely need to install Brew first:
https://brew.sh/


# Find a good sized, well formatted geoJson.

I like the Bing building footprint dataset:

https://github.com/Microsoft/USBuildingFootprints

Pick a state that you like (smaller states will have faster processing time)

One of the most basic commands is:
"tippecanoe -e outt.mbtiles -zg --drop-densest-as-needed Delaware.geojson"
