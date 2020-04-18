"""--------------------------------------------------------------------------------
StandardizeFieldNames_Layouts.py

Description:
Rename fields to fit standards

Input:
1) A geodatabase or folder holding polygon layers

Output:
1) Feature class with renamed fields and new fields

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  March 12, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inGDB = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

namesDict = {
    "Layout_No" : "LayoutNo",
    "IndexID" : "LayoutNo",
    "Application_Reference_No" : "ApplicationReferenceNo",
    "Applicatio" : "ApplicationReferenceNo",
    "Applicat" : "ApplicationReferenceNo",
    "SiteArea_M" : "SiteArea_M2",
    "SiteArea_H" : "SiteArea_HA",
    "SiteArea_S" : "SiteArea_SF",
    "SiteArea_A" : "SiteArea_ARP",
    "ProposedLa" : "ProposedLanduse",
    "ProposedLanduseType" : "ProposedLanduse"
    }

arcpy.AddMessage("Searching the folder now...")

ftrs = []

# Walk GDB and list all polygon features
for dirpath, dirnames, filenames in arcpy.da.Walk(inGDB, datatype="FeatureClass", type="Polygon"):
    for filename in filenames:
        ftrs.append(os.path.join(dirpath, filename))
        ftrCount = len(ftrs)
        arcpy.SetProgressor("step", "Renaming fields...", 0, ftrCount, 1) # Set the progressor
        for ftr in ftrs: # Pass qualified ftrs to list fields
            field_names = [f.name for f in arcpy.ListFields(ftr)]
            for field_name in field_names: # Check if listed fields are in name dict
            	if field_name in namesDict: # If field is in dict, rename field
                    arcpy.AlterField_management(ftr, field_name, namesDict[field_name])
                    arcpy.AddMessage("{0} is in {1}. Renaming now...".format(field_name, ftr))
                    arcpy.SetProgressorPosition() # Update the progressor position
            	else:
                    continue
                    arcpy.AddMessage("{0} is not in {1}.".format(field_name, ftr))
                    arcpy.SetProgressorPosition()
