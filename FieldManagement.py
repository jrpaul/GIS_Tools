"""--------------------------------------------------------------------------------
FieldManagement.py

Description:
Delete and re-create fields.

Input:
1) A geodatabase or folder holding with application points.

Output:
1) Feature class with renames fields and new fields.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  September 30, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inGDB = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

arcpy.AddMessage("Searching the geodatabase now...")

fcList = arcpy.ListFeatureClasses("*", "point")

fcCount = len(fcList)

arcpy.AddMessage("{0} application points layers in this geodatabase.".format(fcCount))

fnamesDict = {
    "Applicant_" : "Applicant_",
    "Applicatio" : "Applicatio",
    "Applicant1" : "Applicant1",
    "Applicat_1" : "Applicat_1",
    "ApplicantLandName" : "ApplicantLandName",
    "Submission" : "Submission",
    "Site_Locat" : "Site_Locat",
    "Site_Loc_1" : "Site_Loc_1",
    "Site_Loc_2" : "Site_Loc_2",
    "X_Coordina" : "X_Coordina",
    "Y_Coordina" : "Y_Coordina",
    "Community_" : "Community_",
    "Submissi_1" : "Submissi_1",
    "Area_Munic" : "Area_Munic",
    "Developmen" : "Developmen",
    "Layout_No" : "Layout_No",
    "Decision_" : "Decision_",
    "Decision"	: "Decision",
    "Decision_D" : "Decision_D",
    "Cadastral_" : "Cadastral_",
    "Enumeratio" : "Enumeratio",
    "Planned_La" : "Planned_La",
    "Planning_R" : "Planning_R",
    "Regional_O" : "Regional_O",
    "Settlement" : "Settlement",
    "Site_Area_" : "Site_Area_",
    "Site_Area1" : "Site_Area1",
    "Total_No__" : "Total_No__",
    "Year_of_Su" : "Year_of_Su",
    "Resource_I" : "Resource_I",
    "Update_Cov" : "Update_Cov",
    "URL" : "URL",
    "Full_URL" : "Full_URL",
    "Update_Ful" : "Update_Ful",
    "Path"	: "Path",
    "Item_Type" : "Item_Type",
    "Created" : "Created",
    "Verified" : "Verified",
    "File_Size" : "File_Size"
    }

for fc in fcList:# Pass qualified ftrs to list fields
	field_names = [f.name for f in arcpy.ListFields(fc)]
	# Check if listed fields are in name dict
	for field_name in field_names:
		# If field is in dict, delete field
		if field_name in fnamesDict:
			arcpy.DeleteField_management(fc, fnamesDict[field_name])
			arcpy.AddMessage("{0} is in {1}. Deleting now...".format(field_name, fc))

# Use list to add fields
for fc in fcList:
    arcpy.management.AddFields(
    fc,
    [['ApplicantFirstName', 'TEXT', 'Applicant First Name', 255],
    ['ApplicantLastName', 'TEXT', 'Applicant Last Name', 255],
    ['SubmissionDate', 'DATE', 'Submission Date'],
    ['SiteLocationLP', 'TEXT', 'Site Location LP', 255],
    ['SiteLocationLot', 'TEXT', 'Site Location Lot', 255],
    ['SiteLocationStreet', 'TEXT', 'Site Location Street', 255],
    ['X_Coordinates', 'DOUBLE', 'X Coordinates'],
    ['Y_Coordinates', 'DOUBLE', 'Y Coordinates'],
    ['CommunityDistrict', 'TEXT', 'Community/District', 255],
    ['SubmissionType', 'TEXT', 'Submission Type', 255],
    ['AreaMunicipal', 'TEXT', 'Area/Municipal', 255],
    ['DevelopmentCategory', 'TEXT', 'Development Category', 255],
    ['Layout_No', 'TEXT', 'Layout No', 255],
    ['Decision', 'TEXT', 'Decision', 255],
    ['DecisionDate', 'DATE', 'Decision Date'],
    ['CadastralSheetNo', 'TEXT', 'Cadastral Sheet No', 255],
    ['EnumerationDistrictNo', 'TEXT', 'Enumeration District No', 255],
    ['PlannedLanduse', 'TEXT', 'Planned Landuse', 255],
    ['PlanningRegion', 'TEXT', 'Planning Region', 255],
    ['Policy', 'TEXT', 'Policy', 255],
    ['RegionalOffice', 'TEXT', 'Regional Office', 255],
    ['SettlementArea', 'TEXT', 'Settlement Area', 255],
    ['SiteArea_M2', 'DOUBLE', 'Site Area M2', 255],
    ['SiteArea_HA', 'DOUBLE', 'Site Area HA', 255],
    ['TotalNoLots', 'DOUBLE', 'Total No Lots', 255],
    ['Year_of_Submission', 'TEXT', 'Year of Submission', 255],
    ['FullURL', 'TEXT', 'Full URL', 255]])

    arcpy.AddMessage("Fields added for {0}".format(fc))
