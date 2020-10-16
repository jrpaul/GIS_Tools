"""--------------------------------------------------------------------------------
ReprojectFCs.py

Description:
Check all fc spatial reference and reproject feature classes to WGS 1984 UTM Zone 20N (32620) where necessary.

Input:
1) A geodatabase or folder holding with application points.

Output:
1) Reprojected feature classes in outputGDB

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  October 14, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inGDB = arcpy.GetParameterAsText(0)
outGDB = arcpy.GetParameterAsText(1)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

arcpy.AddMessage("Searching the geodatabase now...")

fcList = arcpy.ListFeatureClasses()

for fc in fcList:
    spatial_ref = arcpy.Describe(fc).spatialReference
    coords_psc = spatial_ref.PCSName
    #coords_gsc = spatial_ref.GCSName
    arcpy.AddMessage("{0} SR is {1}".format(fc, coords_psc))
    
    if coords_psc == 'WGS_1984_Web_Mercator_Auxiliary_Sphere':
        arcpy.AddMessage("{0} need to be reprojected".format(fc))
        outfc = os.path.join(outGDB, fc)
        outCS = arcpy.SpatialReference('WGS 1984 UTM Zone 20N')
        arcpy.Project_management(fc, outfc, outCS)
    