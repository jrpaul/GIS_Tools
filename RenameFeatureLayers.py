"""--------------------------------------------------------------------------------
Rename Feature Layers.py

Description:
Renames feature classes or shapefiles in a given directory using a user entered character string.

Input:
1) A geodatabase or folder holding feature classes or shapefiles.
2) Characters to be removed.

Output:
1) Renamed feature layers.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  February 03, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inGDB = arcpy.GetParameterAsText(0)
user_string = arcpy.GetParameterAsText(1)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

fc_list = arcpy.ListFeatureClasses(feature_type = 'Polygon')

for fc in fc_list:
    desc = arcpy.Describe(fc)
    ftr_name = desc.Name
    if user_string in ftr_name:
        out_filename = ftr_name.split(user_string)[-1]
        arcpy.Rename_management(ftr_name, out_filename)
        arcpy.AddMessage("This is name: '{0}' and '{1}'".format(ftr_name, out_filename))
    else:
        arcpy.AddMessage("User string not present for '{0}'".format(ftr_name))
