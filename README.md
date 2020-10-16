# GIS Tools
Tools created for land management processes. 

***

**Parcel_outline.py**
Merge parcels within 5 meters of each other to a single polygon to represent the outline of the individual parcels. Existing outlines are skipped. Also copies two attribute fields from input parcels. 

**ListRasterFiles.py**
This geoprocessing script allows the creation of a text file that lists all rasters in a workspace. The projected coordinate system is also listed for each file. Location of outfile is hardcoded.

**ListLayoutParcels.py**
Creates a text file which lists the name, projected coordinate system and number of records found in polygon feature class. Location of outfile is hardcoded.

**RenameFeatureLayers.py** Removes user entered string from feature name.

**StandardiseFieldNames_Layouts.py**
Checks all polygon features in geodatabase and renames non-standard fields.

**StandardiseFieldNames_Applications.py**
Checks all point features in geodatabase and renames non-standard fields.

**AddNewXYFields.py**
Adds two DOUBLE fields to feature class and calculates POINT_X and POINT_Y.

**CheckforNULLFields.py**
Checks features classes for empty or null fields. 

**CreateAreaDomainsSubtypes.py** and **CreateAppFilesDomains.py**
Creates domains and subtypes on file geodatabases.

**AttributeTransfer.py**
Copies attribute data from Excel sheet to multiple fields in a feature class.


