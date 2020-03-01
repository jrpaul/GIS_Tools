"""--------------------------------------------------------------------------------
Rename Feature Layers.py

Description:
This scripts renames feature classes or shapefiles in a given directory/subdirectory using a user entered character string.

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

inGDB = arcpy.GetParameterAsText(0) #geodatabase/folder with features

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True