"""--------------------------------------------------------------------------------
CheckforNullFields.py

Description:
Check parcel feature classes for empty reference number and layout number fields

Input:
1) A geodatabase holding with parcels

Output:
1) List of parcels with null fields

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  March 12, 2020
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

outTXT = datetime.datetime.now().strftime("C:\Temp\Parcel_Null_Fields_Report_%d-%m-%Y.txt")

parcelFields = ['ApplicationReferenceNo', 'LayoutNo']

# Set the progressor
arcpy.SetProgressor("step", "Checking fields...", 0, parcel_count, 1)

with open(outTXT, 'w') as txtfile:
    txtfile.write("Parcels with nulls in application reference or layout number field" + "\n")

    # Loop through the parcel list and write parcel name to txt file
    for parcel in parcels:
        try:
            with arcpy.da.SearchCursor(parcel, parcelFields) as scursor:
                desc = arcpy.Describe(parcel)
                for row in scursor:
                    if (row[0] is None) or (row[1] is None):
                        txtfile.write(desc.baseName + ", " + "has nulls" + "\n")
                        arcpy.SetProgressorPosition()
                    break
        except:
            txtfile.write(desc.baseName + " " + "does not have specified fields." + "\n")
            arcpy.SetProgressorPosition()
