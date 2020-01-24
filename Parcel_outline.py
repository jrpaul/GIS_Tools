"""--------------------------------------------------------------------------------
Parcel_outline.py

Description:
This scripts generates outlines of parcel polygons. Parcels within 5 meters of each other will be aggregated to create the final polygon.

Input:
1) A geodatabase holding feature classes.

Output:
1) A polygon outline of all merged parcels. The outline polygon has "_outline" in the name.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  January 16, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inGDB = arcpy.GetParameterAsText(0) #geodatabase with features

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

fclist = arcpy.ListFeatureClasses("*", "polygon")

# Find the total count of shapefiles in list
fc_count = len(fclist)

# Set the progressor
arcpy.SetProgressor("step", "Generating outlines...", 0, fc_count, 1)

# Count number of outlines complete
completeCount = 0

for fc in fclist:
    # Outpath for parcel layer copy
    parcelOutline = os.path.join(inGDB, fc + "_" + "outline")

    # Check if outline exists, if exists, delete
    if arcpy.Exists(parcelOutline):
        arcpy.AddMessage("{0} exists, not generating outline.".format(fc))
    else:
        # Use aggregate polygons within 5 meters of each other
        arcpy.AggregatePolygons_cartography(fc, parcelOutline, 5)

        # Update the progressor label for current feature class
        arcpy.SetProgressorLabel("Merged {0}...".format(fc))

        completeCount = completeCount + 1

        # Update the progressor position
        arcpy.SetProgressorPosition()

        arcpy.AddMessage("{0} outlines complete.".format(completeCount))

arcpy.ResetProgressor()
