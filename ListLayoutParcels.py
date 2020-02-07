# Script Name: ListLayoutParcelsv2.py
# Description: 
#
# Inputs: 1) A geodatabase containing parcels feature classes  2)  Directory to save text dump of gdb
#
# Outputs: 1) A text file that lists the parcel name, coordinate system name and parcel count for each feature class. 
# 
# Version 0.2
# Created by: Juel Paul
# Date: 12th January 2020

# Import modules
import arcpy
from arcpy import env
import os
import csv
import datetime

inGDB = arcpy.GetParameterAsText(0) #geodatabase with features

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

arcpy.AddMessage("Searching the geodatabase now...")

ftcls = arcpy.ListFeatureClasses("*", "polygon")

fccount = len(ftcls)

arcpy.AddMessage("{0} feature classes in this geodatabase.".format(fccount))

arcpy.AddMessage("Creating text file now...")

# Open txt file and write header
# outputTXT = open("C:\Temp\ParcelCount_Report.txt", 'w')
outTXT = datetime.datetime.now().strftime("C:\Temp\ParcelCount_Report_%d%m%Y.txt")

# outputTXT.write("layout_name" + ", " + "coordsys" + ", " + "num_parcels" + "\n")

with open(outTXT, 'w') as txtfile:
    txtfile.write("layout_name" + ", " + "coordsys" + ", " + "num_parcels" + "\n")
    
    
    for fc in ftcls:
        #Get names of all feature classes
        desc = arcpy.Describe(fc)
        fc_name = desc.name

        #Get spatial reference of each
        spatial_ref = desc.spatialReference
        coords_psc = spatial_ref.PCSName
        #coords_gsc = spatial_ref.GCSName

        #Get number of rows in feature class
        parcel_count = arcpy.GetCount_management(fc).getOutput(0)

        #arcpy.AddMessage(fc_name + "," + coords_psc + " " + coords_gsc + "," + parcel_count)
        txtfile.write(fc_name + ", " + coords_psc + ", " + parcel_count + "\n")


#outputTXT.write("There are {0} feature classes in the geodatabase.".format(fccount))

#outputTXT.close()