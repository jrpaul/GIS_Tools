"""--------------------------------------------------------------------------------
Parcel_outline.py

Description:
This scripts generates outlines of parcel polygons. Parcels within 5 meters of each other will be aggregated to create the final polygon. Copies two attribute field values to the outline layer.

Input:
1) A geodatabase holding feature classes.

Output:
1) A polygon outline of all merged parcels. The outline polygon has "_outline" in the name.

Version 0.2
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

fclist = [ftr for ftr in arcpy.ListFeatureClasses("*", "polygon") if not ftr.endswith('_outline')]

# Find the total count of shapefiles in list
fc_count = len(fclist)

# Set the progressor
arcpy.SetProgressor("step", "Generating outlines...", 0, fc_count, 1)

# Field names list
fcnames = ['LayoutNo', 'Hyperlink', 'ApplicationReferenceNo']

# Count number of outlines complete
completeCount = 0

for fc in fclist:
    # Outpath for parcel layer copy
    parcelOutline = os.path.join(inGDB, fc + "_" + "outline")

    # Check if outline exists, if exists, delete
    if arcpy.Exists(parcelOutline):
        arcpy.AddMessage("{0} outline already exists.".format(fc))
        completeCount = completeCount + 1
    else:
        # Use aggregate polygons within 5 meters of each other
        arcpy.AggregatePolygons_cartography(fc, parcelOutline, 5)

        # Add reference no, hyperlink and layout no fields
        arcpy.management.AddFields(parcelOutline, [['LayoutNo', 'TEXT', 'LayoutNo', 20, '', ''], ['Hyperlink', 'TEXT', 'Hyperlink', 150, '', ''], ['ApplicationReferenceNo', 'TEXT', 'Application Reference No', 12, '', '']])

        # Extract layout no and url from fc
        with arcpy.da.SearchCursor(fc, fcnames) as scursor:
            for row in scursor:
                if row[0] is None:
                    continue
                else:
                    layout = row[0]
                    url = row[1]
                    referenceno = row[2]

        # Update outline fields with values from fc
        with arcpy.da.UpdateCursor(parcelOutline, fcnames) as ucursor:
            for row in ucursor:
                row[0] = layout
                row[1] = url
                row[2] = referenceno
                ucursor.updateRow(row)
            arcpy.AddMessage("Outline updated.")

        # Update the progressor label for current feature class
        arcpy.SetProgressorLabel("Merged {0}...".format(fc))

        completeCount = completeCount + 1

        # Update the progressor position
        arcpy.SetProgressorPosition()

        arcpy.AddMessage("{0} outlines complete.".format(completeCount))

arcpy.ResetProgressor()
