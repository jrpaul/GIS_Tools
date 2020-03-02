"""--------------------------------------------------------------------------------
Rename Feature Layers.py

Description:
Renames feature classes or shapefiles in a given directory/subdirectory using a user entered character string.

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

fc_list = arcpy.ListFeatureClasses(feature_type='Polygon')
for fc in fc_list:
    desc = arcpy.Describe(fc)
    ftr_name = desc.Name
    out_filename = ftr_name.split(user_string)[-1]
    arcpy.Rename_management(ftr_name, out_filename)
    arcpy.AddMessage("This is name: '{0}'".format(name))
        #arcpy.Rename_management(fc, out_filename)
        #arcpy.AddMessage("Renamed '{0}' to '{1}'".format(fc, name))
        #else:
            #arcpy.AddMessage("String '{0}' not found in '{1}'".format(user_string, filename))
