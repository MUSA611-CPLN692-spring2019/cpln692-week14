# Creating GeoJSON to Vector Tiles with Tippecanoe then serving them with a local Python http server


### Step 1: Install Tippecanoe

https://github.com/mapbox/tippecanoe

You will likely need to install Brew first:
https://brew.sh/


### Step 2: Find a good sized, well-formatted geoJson.

I like the Bing building footprint dataset:

https://github.com/Microsoft/USBuildingFootprints

Pick a state that you like (smaller states will have faster processing time)

### Step 3: Run the tippecanoe command line tool

One of the most basic commands is:
`tippecanoe -e outt.mbtiles -zg --drop-densest-as-needed Delaware.geojson`

### Step 4: Update the data source url in `delaware-vector-tiles.html` if you are adding a new dataset

### Step 5: Start your Python server

From this directory in the command line; `python server_vt_py.py`

### Step 6: Open `delaware-vector-tiles.html`
