"""--------------------------------------------------------------------------------
RenameFCs.py

Description:
Rename FCs, removing user entered string.

Input:
1) A geodatabase or folder holding with application points.
2) A user entered string.

Output:
1) Renamed feature class.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  October 15, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
from time import strftime
import os

inGDB = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

fcList = arcpy.ListFeatureClasses("*", "point")
fcCount = len(fcList)
arcpy.AddMessage("Count is {0}".format(fcCount))

for fc in fcList:
    oldName = str(fc)
    newName = oldName.replace("_sorted", "")
    arcpy.Rename_management(fc, newName)
    arcpy.AddMessage("{0} has been renamed".format(fc))