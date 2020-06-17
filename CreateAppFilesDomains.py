"""--------------------------------------------------------------------------------
CreateAppFilesDomains.py

Description:
Creates domains for fields: Decision, Proposed Landuse, Policy, Submission Type, Development Category, Settlement Area, Regional Office

Input:
1) A geodatabase with application points

Output:
1) Domains applied to geodatabase

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  May 29, 2020
--------------------------------------------------------------------------------"""

# Import modules
import arcpy
from arcpy import env
import os

inGDB = arcpy.GetParameterAsText(0)

# Set workspace and environment variables
arcpy.env.workspace = inGDB
arcpy.env.overwriteOutput = True

decisionDict = {
	"A" : "A",
	"R" : "R",
	"RU" : "RU",
	"U" : "U",
	"W" : "W"
}

landuseDict = {
	"01" : "Agriculture",
	"02" : "Residential",
	"03" : "Offices",
	"04" : "Trade",
	"05" : "Industrial",
	"06" : "Institutional",
	"07" : "Protective, Health and Welfare",
	"08" : "Public Utilities",
	"09" : "Transporation, Communication and Warehousing",
	"10" : "Recreation/Open Space",
	"11" : "Vacant"
}

policyDict = {
	"R1" : "Residential - very low density",
	"R2" : "Residential - Low density",
	"R3" : "Residential - Average density",
	"R4" : "Residential - Medium density single family",
	"R5" : "Residential - Medium density multi family",
	"R6" : "Residential - High density",
	"R7" : "Residential - Very high density",
	"RR" : "Resort residential",
	"C1" : "Commercial - Low intensity neighbourhood",
	"C2" : "Commercial - Medium intensity neighbourhood",
	"C3" : "Commercial - High intensity regional/subregional",
	"C4" : "Commercial - Very high intensity C.B.D.",
	"C5" : "Commercial - Planned shopping centres",
	"CM" : "Community facilities",
	"EN" : "Entertainment facilities",
	"WA" : "Warehousing",
	"P1" : "Reservation/conservation (building/sites)",
	"P2" : "Conservation/preservation (natural environment)",
	"OS" : "Recreation/ Open Space",
	"QR" : "Mining / quarrying",
	"M1" : "Industry - Cottage",
	"M2" : "Industry - Light",
	"M3" : "Industry - Heavy",
	"M4" : "Agro - Industry",
	"IN" : "Institutional",
	"A1" : "Livestock - Dairy cattle (8 ha parcels)",
	"A2" : "Agriculture - Extensive 4 ha tree crops, small livestock",
	"A3" : "Agriculture - Mixed (large sugarcane, citrus)",
	"A4" : "Agriculture - Mixed small farms 1.2 ha vegetables, pigs",
	"A5" : "Agriculture - Intensive (.5 ha vegetables)",
	"RA" : "Ribbon Development in Agriculture",
	"S1" : "Special use District",
	"U1" : "Utilities"
}

submitTypeDict = {
	"FULL" : "FULL",
	"OUTLINE" : "OUTLINE"
}

devCategoryDict = {
	"BO" : "Building Operations",
	"EO" : "Engineering Operations",
	"MO" : "Mining Operations",
	"OO" : "Other Operations",
	"CL" : "Making a material change of use of land",
	"CB" : "Making a material change of use of building",
	"SL" : "Subdivision of Land",
	"RS" : "Retention of existing building",
	"RU" : "Continuance of use of land",
	"RO" : "Retention on land of other operations",
	"RL" : "Reclamation of land including coastal protection"
}

settlementAreaDict = {
	"A" : "A",
	"B" : "B",
	"C" : "C",
	"D" : "D",
	"E" : "E",
	"F" : "F",
	"G" : "G",
	"H" : "H",
	"J" : "J",
	"K" : "K",
	"L" : "L",
	"M" : "M",
	"N" : "N",
	"O" : "O",
	"P" : "P",
	"Q" : "Q"
}

regionalOfficeDict = {
	"NRO" : "North Regional Office",
	"SRO" : "South Regional Office",
	"ERO" : "Eastern Regional Office"
}

arcpy.AddMessage("Searching the workspace now...")

fcList = []

for dirpath, dirnames, filenames in arcpy.da.Walk(inGDB, datatype="FeatureClass",type="Point"):
    for filename in filenames:
        fcList.append(os.path.join(dirpath, filename))

#fcCount = len(fcList)

try:
    # Create Decision domain
    arcpy.CreateDomain_management(inGDB, "Decision", "Valid decision types", "TEXT", "CODED")
    decisionDomain = "Decision"
    # Add values from Decision dict to domain
    for code in decisionDict:
        arcpy.AddCodedValueToDomain_management(inGDB, decisionDomain, code, decisionDict[code])
    
    arcpy.AddMessage("Decision domain created.")

except:
	arcpy.AddMessage("Decision domain was not created.")

try:    
    # Create Landuse domain
    arcpy.CreateDomain_management(inGDB, "Landuse", "Valid landuse types", "TEXT", "CODED")
    landuseDomain = "Landuse"
    # Add values from Landuse dict to domain
    for code in landuseDict:
        arcpy.AddCodedValueToDomain_management(inGDB, landuseDomain, code, landuseDict[code])
    
    arcpy.AddMessage("Landuse domain created.")

except:
	arcpy.AddMessage("Landuse domain was not created.")

try:
    # Create Submission type domain
    arcpy.CreateDomain_management(inGDB, "SubmissionType", "Valid submission types", "TEXT", "CODED")
    submissionDomain = "SubmissionType"
    # Add values from submitType dict to domain
    for code in submitTypeDict:
        arcpy.AddCodedValueToDomain_management(inGDB, submissionDomain, code, submitTypeDict[code])
    
    arcpy.AddMessage("Submission Type domain created")

except:
    arcpy.AddMessage("Landuse domain was not created.")

try:
    # Create Development category type domain
    arcpy.CreateDomain_management(inGDB, "DevelopmentCatType", "Valid developement types", "TEXT", "CODED")
    developmentDomain = "DevelopmentCatType"
    # Add values from devCategory dict to domain
    for code in devCategoryDict:
        arcpy.AddCodedValueToDomain_management(inGDB, developmentDomain, code, devCategoryDict[code])
    
    arcpy.AddMessage("Development Category type domain created.")

except:
    arcpy.AddMessage("Landuse domain was not created.")

try:
    # Create Settlement area domain
    arcpy.CreateDomain_management(inGDB, "SettlementArea", "Valid settlement areas", "TEXT", "CODED")
    settlementDomain = "SettlementArea"
    # Add values from settlementArea dict to domain
    for code in settlementAreaDict:
        arcpy.AddCodedValueToDomain_management(inGDB, settlementDomain, code, settlementAreaDict[code])
    
    arcpy.AddMessage("Settlement area domain created.")

except:
    arcpy.AddMessage("Settlement domain was not created.")

try:
    # Create Regional office domain
    arcpy.CreateDomain_management(inGDB, "RegionalOffice", "Valid regional office names", "TEXT", "CODED")
    regofficeDomain = "RegionalOffice"
    # Add values from regionalOffice dict to domain
    for code in regionalOfficeDict:
        arcpy.AddCodedValueToDomain_management(inGDB, regofficeDomain, code, regionalOfficeDict[code])
    
    arcpy.AddMessage("Regional Office domain created.")

except:
	arcpy.AddMessage("Regional office domain was not created.")

try:
    for fc in fcList:
        # Assign domains to fields
        arcpy.AssignDomainToField_management(fc, "Decision", decisionDomain)
        
        arcpy.AddMessage("Domian applied to Decision field.")

        arcpy.AssignDomainToField_management(fc, "PlannedLanduse", landuseDomain)
        
        arcpy.AddMessage("Domian applied to Landuse field.")

        arcpy.AssignDomainToField_management(fc, "SubmissionType", submissionDomain)
        
        arcpy.AddMessage("Domian applied to Submission type field.")

        arcpy.AssignDomainToField_management(fc, "DevelopmentCategory", developmentDomain)
        
        arcpy.AddMessage("Domian applied to Development type field.")

        arcpy.AssignDomainToField_management(fc, "SettlementArea", settlementDomain)
        
        arcpy.AddMessage("Domian applied to Settlement area field.")

        arcpy.AssignDomainToField_management(fc, "RegionalOffice", regofficeDomain)
        
        arcpy.AddMessage("Domian applied to Regional office field.")
except:
    arcpy.AddMessage("Domain was not assigned to field in {0}.".format(fc))