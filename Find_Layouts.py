"""--------------------------------------------------------------------------------
Find_Layouts.py

Description:
Locate layouts (geo-tiffs) in multiple directories

Input:
1) A geodatabase or folder holding geo-tiffs

Output:
1) A text file that lists the layout name, coordinate system name (psc)

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
arcpy.env.workspace = inFLD
arcpy.env.overwriteOutput = True

geolayouts = []

for dirpath, dirnames, filenames in arcpy.da.Walk(inFLD, datatype="RasterDataset"):
    for filename in filenames:
        geolayouts.append(os.path.join(dirpath, filename))

layout_count = len(geolayouts)

arcpy.AddMessage("There are {0} layouts in '{1}'.".format(layout_count, inFLD))

Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')

outTXT = datetime.datetime.now().strftime("C:\Temp\All_GeoLayouts_Report_%d-%m-%Y.txt")

with open(outTXT, 'w') as txtfile:
    txtfile.write("geolayout_name" + ", " + "coordsys" + "\n")

    # Loop through the geolayout list and write layout name and project coord to txt file
    for layout in geolayouts:
        try:
            geolayout_name = os.path.basename(layout) # Extract only the layout basename
            desc = arcpy.Describe(layout)
            spatial_ref = desc.spatialReference
            coords_psc = spatial_ref.PCSName
            txtfile.write(desc.baseName + ", " + coords_psc + "\n")
        except:
            txtfile.write(desc.baseName + " " + "has a problem." + "\n")

#top_directory = os.path.basename(inFLD)
#rename_txt = os.rename(outTXT, os.path.join("All_GeoLayouts_Report_" + top_directory + Current_Date + ".txt"))
