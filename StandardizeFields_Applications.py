"""--------------------------------------------------------------------------------
StandardizeFields_Applications.py

Description:
Rename fields to fit standards.

Input:
1) A geodatabase or folder holding with application points.

Output:
1) Feature class with renames fields and new fields.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  March 18, 2020
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
    "Name_" : "Name",
    "File_Refer" : "FileReferenceNo",
    "Application_Reference_No" : "ApplicationReferenceNo",
    "Reference_" : "ApplicationNumber",
    "Applicant_" : "ApplicantFirstName",
    "Applicatio" : "ApplicantFirstName",
    "Applicant1" : "ApplicantLastName",
    "Applicat_1" : "ApplicantLastName",
    "ApplicantLandName" : "ApplicantLastName",
    "Submission" : "ReceivedDate",
    "Site_Locat" : "SiteLocationLP",
    "Site_Loc_1" : "SiteLocationLotNo",
    "Site_Loc_2" : "SiteLocationStreet",
    "X_Coordina" : "X_Coordinates",
    "Y_Coordina" : "Y_Coordinates",
    "Community_" : "CommunityDistrict",
    "Submissi_1" : "SubmissionType",
    "Area_Munic" : "AreaMunicipal",
    "Developmen" : "DevelopmentCategory",
    "Layout_No" : "Layout_No",
    "Decision_" : "Decision",
    "Decision_D" : "DecisionDate",
    "Cadastral_" : "CadastralSheetNo",
    "Enumeratio" : "EnumerationDistrictNo",
    "Planned_La" : "PlannedLanduse",
    "Planning_R" : "PlanningRegion",
    "Regional_O" : "RegionalOffice",
    "Settlement" : "SettlementArea",
    "Site_Area_" : "SiteArea_M2",
    "Site_Area1" : "SiteArea_HA",
    "Total_No__" : "TotalNoLots",
    "Year_of_Su" : "Year_of_Submission",
    "Resource_I" : "Resource_Identifer",
    "Update_Cov" : "Update_Coverage",
    "Full_URL" : "FullURL",
    "Update_Ful" : "UpdateFullApplicationURL",
    "Transform_" : "Transform_X",
    "Transform1" : "Transform_Y",
    "TRANSFORM_" : "Transform_X",
    "TRANSFORM1" : "Transform_Y"
    }

arcpy.AddMessage("Searching the folder now...")

ftrs = []
checkCount = 0
fixedCount = 0

# Walk GDB and list all point layers
for dirpath, dirnames, filenames in arcpy.da.Walk(inGDB, datatype="FeatureClass", type="Point"):
    for filename in filenames:
        ftrs.append(os.path.join(dirpath, filename))
        ftrCount = len(ftrs)

arcpy.AddMessage("There are {0} feature classes in the geodatabase".format(ftrCount))

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

arcpy.AddMessage("{0} fields were renamed and {1} fields were not renamed.".format(fixedCount, checkCount))
