"""--------------------------------------------------------------------------------
Find_Parcels.py

Description:
Check directories for polygon layers

Input:
1) A geodatabase or folder holding with parcels

Output:
1) A text file that lists the parcel name, coordinate system name and parcel count for each feature class.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  March 15, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inFLD = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inFLD
arcpy.env.overwriteOutput = True

parcels = []

for dirpath, dirnames, filenames in arcpy.da.Walk(inFLD, datatype="FeatureClass",type="Polygon"):
    for filename in filenames:
        parcels.append(os.path.join(dirpath, filename))

parcel_count = len(parcels)

arcpy.AddMessage("There are {0} parcels in '{1}'.".format(parcel_count, inFLD))

Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')

outTXT = datetime.datetime.now().strftime("C:\Temp\All_Parcels_Report_%d-%m-%Y.txt")

with open(outTXT, 'w') as txtfile:
    txtfile.write("layout_name" + ", " + "coordsys" + ", " + "num_parcels" + "\n")

    for parcel in parcels:
        try:
            parcel_name =  os.path.basename(parcel) # Extract only the parcel basename
            desc = arcpy.Describe(parcel)

            #Get spatial reference of each
            spatial_ref = desc.spatialReference
            coords_psc = spatial_ref.PCSName
            #coords_gsc = spatial_ref.GCSName

            #Get number of rows in feature class
            feature_count = arcpy.GetCount_management(parcel).getOutput(0)

            #arcpy.AddMessage(parcel_name + "," + coords_psc + " " + coords_gsc + "," + parcel_count)
            txtfile.write(parcel_name + ", " + coords_psc + ", " + feature_count + "\n")
        except:
            txtfile.write(parcel_name + " " + "has a problem." + "\n")
