"""--------------------------------------------------------------------------------
AddNewXYFields.py

Description:
Add new fields, New_X and New_Y fields and calculate the X and Y coords

Input:
1) A geodatabase or folder holding polygon layers

Output:
1) Feature class with new fields

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  March 18, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env

inGDB = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

arcpy.AddMessage("Searching the geodatabase now...")

fcList = arcpy.ListFeatureClasses("*", "point")

fcCount = len(fcList)

arcpy.AddMessage("{0} application points in this geodatabase.".format(fcCount))

# Use list to add fields and calculate XY
for fc in fcList:
    arcpy.management.AddFields(
    fc, 
    [['New_X', 'DOUBLE', 'New X'],
    ['New_Y', 'DOUBLE', 'New Y']])

    arcpy.CalculateGeometryAttributes_management(fc,
        [["New_X", "POINT_X"], ["New_Y", "POINT_Y"]])

    arcpy.AddMessage("Fields added and geometry calulated for {0}".format(fc))
