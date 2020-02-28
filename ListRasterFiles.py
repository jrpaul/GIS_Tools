# Script Name: ListRasterFiles.py
# Description:
#
# Inputs: 1) A folder containing tif files
#
# Outputs: 1) A text file that lists the layout name and projected coordinate system name.
#
# Script expects C:\Temp directory
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

inFLD = arcpy.GetParameterAsText(0) #folder with features

# Set workspace and environment variables
arcpy.env.workspace = inFLD
arcpy.env.overwriteOutput = True


arcpy.AddMessage("Searching the folder now...")

rsts = arcpy.ListRasters("*", "TIF")

rstcount = len(rsts)

arcpy.AddMessage("{0} layouts in this folder.".format(rstcount))

arcpy.AddMessage("Creating text file...")

outTXT = datetime.datetime.now().strftime("C:\Temp\LayoutPlans_Report_%d%m%Y.txt")

# Create txt file appended with date then write header
# outputTXT = open("C:\Temp\LayoutParcels_Report.txt", 'w')

with open(outTXT, 'w') as txtfile:
    txtfile.write("geolayout_name" + ", " + "coordsys" + "\n")

    for rst in rsts:
        #Get names of all rasters
        desc = arcpy.Describe(rst)
        rst_name = desc.baseName

        #Get spatial reference of each
        spatial_ref = desc.spatialReference
        coords_psc = spatial_ref.PCSName
        #coords_gsc = spatial_ref.GCSName


        #arcpy.AddMessage(rst_name + "," + coords_psc + " " + coords_gsc)
        #outputCSV.write(rst_name + " , " + coords_psc + " " + coords_gsc)

        txtfile.write(rst_name + ", " + coords_psc + "\n")


#outputTXT.write("{0} layouts in this folder.".format(rstcount))
