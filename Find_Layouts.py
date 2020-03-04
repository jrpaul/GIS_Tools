"""--------------------------------------------------------------------------------
Find_Layouts.py

Description:
Located layouts (geo-tiffs) in multiple directories.

Input:
1) A geodatabase or folder holding geo-tiffs.

Output:
1) List of layouts.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  March 04, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inFLD = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

geolayouts = []
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="RasterDataset",type="TIF"):
    for filename in filenames:
        geolayouts.append(os.path.join(dirpath, filename))

layout_count = len(geolayouts)

outTXT = datetime.datetime.now().strftime("C:\Temp\All_GeoLayouts_Report_%d%m%Y.txt")

with open(outTXT, 'w') as txtfile:
    txtfile.write("geolayout_name" + ", " + "coordsys" + "\n")
    
    # Loop through the geolayout list and write layout name and project coord to txt file
    for layout in geolayouts:
        geolayout_name = os.path.basename(layout) # Extract only the layout basename
        spatial_ref = os.path.spatialReference(layout)
        coords_psc = spatial_ref.PCSName(layout)
        
        txtfile.write(geolayout_name + ", " + coords_psc + "\n")