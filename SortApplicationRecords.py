"""--------------------------------------------------------------------------------
SortApplicationRecords.py

Description:
Sort application records by reference number for all point files in geodatabase.

Input:
1) A geodatabase with application points


Version 0.1
Created by: Juel Paul/Land Analytical
Date:  June 7, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inGDB = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

arcpy.AddMessage("Searching the input workspace now...")

fcList = arcpy.ListFeatureClasses("*", "point")

fcCount = len(fcList)

arcpy.AddMessage("There are {0} layers in the workspace".format(fcCount))

# Set the progressor
arcpy.SetProgressor("step", "Sorting now...", 0, fcCount, 1)

for fc in fcList:
	try:
		outPath = os.path.join(inGDB + "\\" + fc + "_sorted")
		arcpy.Sort_management(fc, outPath, [["ApplicationNumber", "ASCENDING"]])

		arcpy.SetProgressorPosition()

		arcpy.AddMessage("{0} has been sorted".format(fc))
	except:
		arcpy.AddMessage("{0} has a problem".format(fc))

		arcpy.SetProgressorPosition()

arcpy.AddMessage("Sort is complete.")
