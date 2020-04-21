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
checkCount = 0
fixedCount = 0

# Walk GDB and list all polygon features
for dirpath, dirnames, filenames in arcpy.da.Walk(inGDB, datatype="FeatureClass", type="Polygon"):
    for filename in filenames:
        ftrs.append(os.path.join(dirpath, filename))
        ftrCount = len(ftrs)

for ftr in ftrs:# Pass qualified ftrs to list fields
    field_names = [f.name for f in arcpy.ListFields(ftr)]
    # Check if listed fields are in name dict
    for field_name in field_names:
        # If field is in dict, rename field
        if field_name in namesDict:
            arcpy.AlterField_management(ftr, field_name, namesDict[field_name], "", "", "", "", "TRUE")
            arcpy.AddMessage("{0} is in {1}. Renaming now...".format(field_name, ftr))
            fixedCount = fixedCount + 1
        else:
            arcpy.AddMessage("{0} in {1} does not need renaming.".format(field_name, ftr))
            checkCount = checkCount + 1

arcpy.AddMessage("{0} fields checked and {1} fields renamed.".format(checkCount, fixedCount))
