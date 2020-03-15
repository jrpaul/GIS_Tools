# GIS Tools
Tools created for land analytical processes. 

***

**Amalgamate Parcels.py**
This is an ArcGIS Pro geoprocessing script to quickly merge parcels within 5 meters of each other to a single polygon which represents the outline of the individual parcels. The workspace must be set to a geodatabase. Existing outlines are skipped. Also copies two attribute fields from input parcels. 

**List Raster Files.py**
This geoprocessing script allows the creation of a text file that list all rasters in a workspace. The projected coordinate system is also listed for each file. Location of outfile is hardcoded.

**List Layout Parcels.py**
Creates a text file which list the name, projected coordinate system and number of records found in polygon feature class. Workspace is set to be a geodatabase. Location of outfile is hardcoded.

**StandardiseFields_Layouts.py**
Checks all polygon features in geodatabase and renames non-standard fields.
