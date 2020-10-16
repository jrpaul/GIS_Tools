"""--------------------------------------------------------------------------------
AttributeTransfer.py

Description:
Transfer updated attribute data in Excel sheet to empty feature class fields.

Input:
1) A geodatabase or folder holding with application points.
2) Excel table with updated attribute data

Output:
1) Updated feature class.

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  October 14, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
from time import strftime
import os

inGDB = arcpy.GetParameterAsText(0)
sourceTB = arcpy.GetParameterAsText(1)
updateFC = arcpy.GetParameterAsText(2)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True


sourceFieldsList = ["Reference_No", "Applicant_First_Name", "Applicant_Last_Name", "Submission_Date", "Site_Location_L_P_", "Site_Location_Lot_No_", "Site_Location_Street", "X_Coordinates", "Y_Coordinates", "Community_District", "Submission_Type", "Area_Municipal", "Development_Category__Code_", "Layout_No", "Decision", "Decision_Date", "Cadastral_No_", "Enumeration_District_No", "Planned_Land_Use", "Policy", "Planning_Region", "Regional_Office", "Settlement_Area", "Site_Area_M2", "Site_Area_HA", "Total_No__of_Lots", "Year_of_Submission", "Full_URL"]

# Use list comprehension to build a dictionary from a da SearchCursor
valueDict = {r[0]:(r[1:]) for r in arcpy.da.SearchCursor(sourceTB, sourceFieldsList)}


updateFieldsList = ["Reference_", "ApplicantFirstName", "ApplicantLastName", "SubmissionDate", "SiteLocationLP", "SiteLocationLot", "SiteLocationStreet", "X_Coordinates", "Y_Coordinates", "CommunityDistrict", "SubmissionType", "AreaMunicipal", "DevelopmentCategory", "Layout_No", "Decision", "DecisionDate", "CadastralSheetNo", "EnumerationDistrictNo", "PlannedLanduse", "Policy", "PlanningRegion", "RegionalOffice", "SettlementArea", "SiteArea_M2", "SiteArea_HA", "TotalNoLots", "Year_of_Submission", "FullURL"]

with arcpy.da.UpdateCursor(updateFC, updateFieldsList) as updateRows:
    for updateRow in updateRows:
        # store the Join value of the row being updated in a keyValue variable
        keyValue = updateRow[0]
        # verify that the keyValue is in the Dictionary
        if keyValue in valueDict:
            # transfer the values stored under the keyValue from the dictionary to the updated fields.
            updateRow[1] = valueDict[keyValue][0]
            updateRow[2] = valueDict[keyValue][1]
            updateRow[3] = valueDict[keyValue][2]
            updateRow[4] = valueDict[keyValue][3]
            updateRow[5] = valueDict[keyValue][4]
            updateRow[6] = valueDict[keyValue][5]
            updateRow[7] = valueDict[keyValue][6]
            updateRow[8] = valueDict[keyValue][7]
            updateRow[9] = valueDict[keyValue][8]
            updateRow[10] = valueDict[keyValue][9]
            updateRow[11] = valueDict[keyValue][10]
            updateRow[12] = valueDict[keyValue][11]
            updateRow[13] = valueDict[keyValue][12]
            updateRow[14] = valueDict[keyValue][13]
            updateRow[15] = valueDict[keyValue][14]
            updateRow[16] = valueDict[keyValue][15]
            updateRow[17] = valueDict[keyValue][16]
            updateRow[18] = valueDict[keyValue][17]
            updateRow[19] = valueDict[keyValue][18]
            updateRow[20] = valueDict[keyValue][19]
            updateRow[21] = valueDict[keyValue][20]
            updateRow[22] = valueDict[keyValue][21]
            updateRow[23] = valueDict[keyValue][22]
            updateRow[24] = valueDict[keyValue][23]
            updateRow[25] = valueDict[keyValue][24]
            updateRow[26] = valueDict[keyValue][25]
            updateRow[27] = valueDict[keyValue][26]
            updateRows.updateRow(updateRow)
        else:
        	pass

del valueDict
