"""--------------------------------------------------------------------------------
CreateAreaDomainsSubtypes.py

Description:
Creates domains and subtypes for planning areas

Input:
1) A geodatabase with application points

Output:
1) Domains applied to geodatabase

Version 0.1
Created by: Juel Paul/Land Analytical
Date:  June 12, 2020
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

t1CommsDict = {
    "1" : "Alyce Glen",
    "2" : "Bagatelle",
    "3" : "Bayshore",
    "4" : "Beau Pres",
    "5" : "Beetham Estate",
    "6" : "Bejucal",
    "7" : "Belmont",
    "8" : "Big Yard",
    "9" : "Blue Basin",
    "10" : "Blue Range",
    "11" : "Boissiere",
    "12" : "Cameron Road",
    "13" : "Carenage",
    "14" : "Cascade",
    "15" : "Chaguaramas",
    "16" : "Champ Elysees",
    "17" : "Cocorite",
    "18" : "Covigne",
    "19" : "Diamond Vale",
    "20" : "Dibe/Belle Vue",
    "21" : "Diego Martin Proper",
    "22" : "East Port Of Spain",
    "23" : "Eastern Quarry",
    "24" : "El Socorro Extension",
    "25" : "Ellerslie Park",
    "26" : "Fairways",
    "27" : "Federation Park",
    "28" : "Fort George",
    "29" : "Four Roads",
    "30" : "Glencoe",
    "31" : "Goodwood Gardens",
    "32" : "Green Hill Village",
    "33" : "Haleland Park/Moka",
    "34" : "Industrial Estate",
    "35" : "La Horquette",
    "36" : "La Pastora",
    "37" : "La Puerta",
    "38" : "La Seiva",
    "39" : "Lady Chancellor",
    "40" : "Lanse Mitan",
    "41" : "Las Cuevas",
    "42" : "Laventille",
    "43" : "Le Platte",
    "44" : "Long Circular",
    "45" : "Maracas",
    "46" : "Maracas Bay",
    "47" : "Maraval Proper",
    "48" : "Marie Road",
    "49" : "Mon Repos",
    "50" : "Morvant",
    "51" : "Never Dirty",
    "52" : "North Post",
    "53" : "Paramin",
    "54" : "Patna Village",
    "55" : "Petit Valley",
    "56" : "Picton",
    "57" : "Point Cumana",
    "58" : "Port Of Spain Port Area",
    "59" : "Port Of Spain Proper",
    "60" : "Powder Magazine",
    "61" : "Rich Plain",
    "62" : "Romain Lands",
    "63" : "Saut Deau",
    "64" : "Sealots",
    "65" : "Simeon Road",
    "66" : "St. Anns",
    "67" : "St. Barbs",
    "68" : "St. Clair",
    "69" : "St. James",
    "70" : "St. Lucien Road",
    "71" : "Upper Belmont",
    "72" : "Upper St. James",
    "73" : "Victoria Gardens",
    "74" : "Water Hole",
    "75" : "West Moorings",
    "76" : "Woodbrook"
}

t2CommsDict = {
    "1" : "Acono Village",
    "2" : "Aranguez",
    "3"	: "Arouca",
    "4"	: "Bamboo Grove",
    "5"	: "Barataria",
    "6"	: "Beetham Estate",
    "7"	: "Bejucal",
    "8"	: "Blanchisseuse",
    "9"	: "Bon Air Development",
    "10" : "Bon Air West Development",
    "11" : "Cane Farm",
    "12" : "Cantaro Village",
    "13": "Carapo",
    "14" : "Caroni Village",
    "15" : "Cascade",
    "16" : "Caura",
    "17" : "Centeno",
    "18" : "Champ Fleurs",
    "19" : "Curepe",
    "20" : "D'abadie", 
    "21" : "Dinsley", 
    "22" : "Dinsley/Trincity",
    "23" : "El Dorado",
    "24" : "El Socorro",
    "25" : "El Socorro Extension", 
    "26" : "Eric Williams Medical Sciences Complex",
    "27" : "Febeau Village", 
    "28" : "Five Rivers",
    "29" : "Frederick Settlement",
    "30" : "Gran Curucaye",
    "31" : "Haleland Park/Moka",
    "32" : "Kandahar",
    "33" : "Kelly Village",
    "34" : "La Baja",
    "35" : "La Canoa",
    "36" : "La Florisante",
    "37" : "La Mango Village",
    "38" : "La Paille Village",
    "39" : "La Pastora",
    "40" : "La Resource",
    "41" : "La Seiva Village",
    "42" : "Las Cuevas",
    "43" : "Laventille",
    "44" : "Lopinot Village",
    "45" : "Lower Santa Cruz",
    "46" : "Macoya",
    "47" : "Malick",
    "48" : "Maloney Gardens",
    "49" : "Maracas",
    "50" : "Maracas/St. Joseph",
    "51" : "Mausica",
    "52" : "Mon Repos",
    "53" : "Morvant",
    "54" : "Mount D\'or",
    "55" : "Mount St. Benedict",
    "56" : "Mt. Hope",
    "57" : "Mt. Lambert",
    "58" : "Oropuna Village/Piarco",
    "59" : "Paradise Gardens",
    "60" : "Pasea Extension",
    "61" : "Petit Bourg",
    "62" : "Real Springs",
    "63" : "Redhill",
    "64" : "Sam Boucaud",
    "65" : "San Juan",
    "66" : "Santa Cruz",
    "67" : "Santa Margarita",
    "68" : "Soconusco",
    "69" : "Spring Village",
    "70" : "St. Anns",
    "71" : "St. Augustine",
    "72" : "St. Augustine South",
    "73" : "St. John\'s Village",
    "74" : "St. Joseph",
    "75" : "Surrey Village",
    "76" : "Tacarigua",
    "77" : "Tacarigua",
    "78" : "Trincity",
    "79" : "Tunapuna",
    "80" : "Valley View",
    "81" : "Valsayn"

}

t3CommsDict = {
    "1"	: "Arima Heights/Temple Village",
    "2"	: "Arima Proper",
    "3"	: "Blanchisseuse",
    "4"	: "Brasso Seco Village",
    "5"	: "Calvary Hill",
    "6"	: "Carapo",
    "7"	: "Carib Homes",
    "8"	: "Cleaver Road",
    "9"	: "D\'abadie",
    "10" : "Heights Of Guanapo",
    "11" : "La Florisante",
    "12" : "La Horquetta",
    "13" : "La Laja",
    "14" : "La Resource",
    "15" : "Las Cuevas",
    "16" : "Malabar",
    "17" : "Maturita",
    "18" : "Mausica",
    "19" : "Mount Pleasant",
    "20" : "Mundo Nuevo",
    "21" : "Olton Road",
    "22" : "O\'meara Road",
    "23" : "Peytonville",
    "24" : "Pinto Road",
    "25" : "Redhill",
    "26" : "Samaroo Village",
    "27" : "San Raphael/Brazil",
    "28" : "Santa Rosa Heights",
    "29" : "Sherwood Park",
    "30" : "Talparo",
    "31" : "Tamana Road",
    "32" : "Tumpuna Road",
    "33" : "Tumpuna Road",
    "34" : "Valencia",
    "35" : "Wallerfield"
}

t4CommsDict = {
    "1"	: "Anglais Settlement",
    "2"	: "Balandra",
    "3"	: "Biche",
    "4"	: "Brooklyn Settlement",
    "5"	: "Caigual",
    "6"	: "Carmichael",
    "7"	: "Coal Mine",
    "8"	: "Cumaca",
    "9"	: "Cumana",
    "10" : "Cumuto",
    "11" : "Cunaripo",
    "12" : "Fishing Pond",
    "13" : "Four Roads - Tamana",
    "14" : "Grand Riviere",
    "15" : "Guaico",
    "16" : "Guatopajaro",
    "17" : "Howsen Village",
    "18" : "L\'anse Noir",
    "19" : "Mahoe",
    "20" : "Manzanilla",
    "21" : "Maraj Hill",
    "22" : "Matelot",
    "23" : "Matura",
    "24" : "Melajo",
    "25" : "Mission",
    "26" : "Monte Video",
    "27" : "Morin Bay",
    "28" : "North Manzanilla",
    "29" : "Oropouche",
    "30" : "Plum Mitan",
    "31" : "Rampanalgas",
    "32" : "Salybia Village",
    "33" : "San Souci",
    "34" : "Sangre Chiquito",
    "35" : "Sangre Grande Proper",
    "36" : "Talparo",
    "37" : "Tamana",
    "38" : "Tamana",
    "39" : "Toco",
    "40" : "Tompire",
    "41" : "Turure",
    "42" : "Valencia"
}

t5CommsDict = {
    "1"	: "Agostini Village",
    "2"	: "Arena",
    "3"	: "Balmain",
    "4"	: "Basta Hall",
    "5"	: "Bejucal",
    "6"	: "Brasso Caparo Village",
    "7"	: "Brasso Manuel Junction",
    "8"	: "Brasso Tamana",
    "9"	: "Brasso Venado",
    "10" : "Brechin Castle",
    "11" : "Brickfield",
    "12" : "Bucarro",
    "13" : "Butler Village",
    "14" : "Calcutta Road No. 2",
    "15" : "Calcutta Settlement No. 2",
    "16" : "California",
    "17" : "Caparo",
    "18" : "Carapichaima",
    "19" : "Carlsen Field",
    "20" : "Chaguanas Proper",
    "21" : "Chandernagore",
    "22" : "Charlieville",
    "23" : "Chase Village",
    "24" : "Chickland",
    "25" : "Chin Chin",
    "26" : "Claxton Bay",
    "27" : "Coal Mine",
    "28" : "Couva Central",
    "29" : "Cunupia",
    "30" : "Dow Village",
    "31" : "Edinburgh 500",
    "32" : "Edinburgh Gardens",
    "33" : "Edinburgh Village",
    "34" : "Endeavour Village",
    "35" : "Enterprise",
    "36" : "Esmeralda",
    "37" : "Esperanza",
    "38" : "Fairview",
    "39" : "Felicity",
    "40" : "Felicity Hall",
    "41" : "Flanagin Town",
    "42" : "Freeport",
    "43" : "Friendship",
    "44" : "Gran Couva",
    "45" : "Homeland Gardens",
    "46" : "Indian Trail",
    "47" : "Jerningham Junction",
    "48" : "Kelly Village",
    "49" : "Lange Park",
    "50" : "Las Lomas (Nos. 1 & 2)",
    "51" : "Lendore Village",
    "52" : "Longdenville",
    "53" : "Madras Settlement",
    "54" : "Mamoral No. 2",
    "55" : "Mc Bean",
    "56" : "Montrose Village",
    "57" : "Mount Pleasant",
    "58" : "Munroe Settlement",
    "59" : "Orange Valley",
    "60" : "Ouplay Village",
    "61" : "Palmiste",
    "62" : "Pepper Village",
    "63" : "Petersfield",
    "64" : "Phoenix Park",
    "65" : "Point Lisas Ind. Estate",
    "66" : "Point Lisas (Nha)",
    "67" : "Point Lisas (Plipdeco Housing)",
    "68" : "Preysal",
    "69" : "Ravine Sable",
    "70" : "Spring Village",
    "71" : "Spring Village",
    "72" : "St. Andrew\'s Village",
    "73" : "St. Charles Village",
    "74" : "St. Helena Village",
    "75" : "St. Mary\'s Village",
    "76" : "St. Thomas Village",
    "77" : "Tabaquite",
    "78" : "Todd\'s Road",
    "79" : "Todd\'s Station",
    "80" : "Warren Village",
    "81" : "Warren Village",
    "82" : "Waterloo",
    "83" : "Welcome"
}

t6CommsDict = {
    "1"	: "Abysinia Village (Oilfield Area)",
    "2" : "Agostini Village",
    "3"	: "Biche",
    "4"	: "Brickfield/Navet",
    "5"	: "Canque",
    "6"	: "Charuma Village",
    "7"	: "Cocal Estate/Mayaro",
    "8"	: "Cushe/Navet",
    "9"	: "Deep Ravine/Clear Water",
    "10" : "Ecclesville",
    "11" : "Fonrose Village",
    "12" : "Four Roads - Tamana",
    "13" : "Grand Lagoon",
    "14" : "Guayaguayare",
    "15" : "La Savanne",
    "16" : "Libertville",
    "17" : "Mafeking",
    "18" : "Mainfield",
    "19" : "Manzanilla",
    "20" : "Mayaro",
    "21" : "Mora Settlement",
    "22" : "Navet Village",
    "23" : "Ortoire",
    "24" : "Plaisance",
    "25" : "Plum Mitan",
    "26" : "Poole",
    "27" : "Radix",
    "28" : "Rio Claro",
    "29" : "Robert Village",
    "30" : "San Pedro",
    "31" : "St. Joseph Village",
    "32" : "St. Mary\'s Village",
    "33" : "Union Village"
}

t7CommsDict = {
    "1"	: "Barrackpore",
    "2"	: "Basse Terre",
    "3"	: "Ben Lomond",
    "4"	: "Bon Jean",
    "5"	: "Bonne Aventure",
    "6"	: "Borde Narve",
    "7"	: "Broadway",
    "8"	: "Broomage",
    "9"	: "Brothers Road",
    "10" : "Brothers Settlement",
    "11" : "Buen Intento",
    "12" : "Canaan Village/Palmiste",
    "13" : "Canaree",
    "14" : "Caratal",
    "15" : "Cedar Hill",
    "16" : "Cedar Hill",
    "17" : "City Proper",
    "18" : "Claxton Bay",
    "19" : "Cleghorn And Mt. Pleasant",
    "20" : "Cocoyea Village",
    "21" : "Corinth",
    "22" : "Corosal",
    "23" : "Coryal Village",
    "24" : "Diamond",
    "25" : "Duncan Village",
    "26" : "Dyers Village",
    "27" : "Eccles Village",
    "28" : "Embacadere",
    "29" : "Esperance Village",
    "30" : "Farnum Village",
    "31" : "Fifth Company",
    "32" : "Fonrose Village",
    "33" : "Forres Park",
    "34" : "Friendship",
    "35" : "Gasparillo",
    "36" : "George Village",
    "37" : "Golconda",
    "38" : "Green Acres",
    "39" : "Guaracara",
    "40" : "Gulf View",
    "41" : "Hard Bargain",
    "42" : "Harmony Hall",
    "43" : "Hermitage",
    "44" : "Hermitage Village",
    "45" : "Hindustan",
    "46" : "Iere Village",
    "47" : "Indian Trail",
    "48" : "Indian Walk",
    "49" : "Jordan Village",
    "50" : "Kumar Village",
    "51" : "La Fortune",
    "52" : "La Lune",
    "53" : "La Romain",
    "54" : "La Ruffin",
    "55" : "La Savanne",
    "56" : "Lengua Village",
    "57" : "Lengua Village/Barrackpore",
    "58" : "Les Efforts East",
    "59" : "Les Efforts West",
    "60" : "Lothian",
    "61" : "Lower Hill Side",
    "62" : "Malgretoute",
    "63" : "Marabella",
    "64" : "Marac",
    "65" : "Maraj Lands",
    "66" : "Matilda",
    "67" : "Mayo",
    "68" : "Mon Repos",
    "69" : "Monkey Town",
    "70" : "Moruga Village",
    "71" : "Navet Village",
    "72" : "New Grant",
    "73" : "Palmiste",
    "74" : "Palmyra",
    "75" : "Palmyra Village/Mt. Stewart",
    "76" : "Paradise",
    "77" : "Parforce",
    "78" : "Petit Cafe",
    "79" : "Petit Morne",
    "80" : "Phillipine",
    "81" : "Picton",
    "82" : "Piparo",
    "83" : "Plaisance Park",
    "84" : "Pleasantville",
    "85" : "Poonah",
    "86" : "Princes Town Proper",
    "87" : "Rambert Village",
    "88" : "Reform Village",
    "89" : "Riversdale",
    "90" : "Robert Village",
    "91" : "Sisters Village",
    "92" : "Sixth Company",
    "93" : "Springland/San Fabian",
    "94" : "St. Charles Village",
    "95" : "St. Clements",
    "96" : "St. Croix Village",
    "97" : "St. John\'s Village",
    "98" : "St. Joseph Village",
    "99" : "St. Julien",
    "100" : "St. Madeline",
    "101" : "St. Margaret",
    "102" : "St. Mary\'s Village",
    "103" : "Sum Sum Hill",
    "104" : "Tableland",
    "105" : "Tarouba",
    "106" : "Tortuga",
    "107" : "Trintoc (Pointe A Pierre)",
    "108" : "Union Park",
    "109" : "Union Village",
    "110" : "Union Village",
    "111" : "Usine St. Madeline",
    "112" : "Victoria Village",
    "113" : "Vistabella",
    "114" : "Wellington",
    "115" : "White Land"
}

t8CommsDict = {
    "1"	: "Apex Oil Field",
    "2"	: "Aripero Village",
    "3"	: "Avocat Village",
    "4"	: "Bamboo Village",
    "5"	: "Barrackpore",
    "6"	: "Basse Terre",
    "7"	: "Batchyia Village",
    "8"	: "Beach Camp",
    "9"	: "Bennet Village",
    "10" : "Bois Bough",
    "11" : "Bonasse Village",
    "12" : "Brighton",
    "13" : "Cap De Ville",
    "14" : "Carapal",
    "15" : "Cedros",
    "16" : "Charlo Village",
    "17" : "Chatham",
    "18" : "Chinese Village",
    "19" : "Clifton Hill",
    "20" : "Cochrane",
    "21" : "Coromandel",
    "22" : "Danny Village",
    "23" : "De Gannes Village",
    "24" : "Delhi Settlement",
    "25" : "Dow Village",
    "26" : "Egypt Village",
    "27" : "Erin Proper",
    "28" : "Erin/Buenos Ayres",
    "29" : "Fanny Village",
    "30" : "Forest Reserve",
    "31" : "Fullerton",
    "32" : "Fyzabad",
    "33" : "Gheerahoo",
    "34" : "Gonzales(Point Fortin)",
    "35" : "Granville",
    "36" : "Guapo Lot 10",
    "37" : "Harris Village",
    "38" : "Hollywood",
    "39" : "Icacos",
    "40" : "Jacob Village",
    "41" : "La Brea",
    "42" : "La Fortune/Pluck",
    "43" : "Lorensotte",
    "44" : "Los Bajos",
    "45" : "Los Charos",
    "46" : "Los Iros/Erin",
    "47" : "Marac",
    "48" : "Mendez Village",
    "49" : "Mon Desir",
    "50" : "Mon Desir/Silver Stream",
    "51" : "Morne Diablo",
    "52" : "New Village",
    "53" : "Newlands",
    "54" : "Oropouche",
    "55" : "Palo Seco",
    "56" : "Parry Lands South",
    "57" : "Penal",
    "58" : "Penal Quinam Beach Road",
    "59" : "Penal Rock Road",
    "60" : "Pepper Village",
    "61" : "Point D\'or",
    "62" : "Point Fortin Proper",
    "63" : "Point Ligoure",
    "64" : "Quarry Village",
    "65" : "Rancho Quemado",
    "66" : "Robert Hill/Siparia",
    "67" : "Rochard Road",
    "68" : "Rousillac",
    "69" : "Salazar Village",
    "70" : "San Francique",
    "71" : "San Francique",
    "72" : "Santa Flora",
    "73" : "Scott Road Village",
    "74" : "Siparia",
    "75" : "Sobo Village",
    "76" : "St. John",
    "77" : "St. Mary\'s Village",
    "78" : "Sudama Village",
    "79" : "Syne Village",
    "80" : "Techier Village",
    "81" : "Thick Village",
    "82" : "Tulsa Village",
    "83" : "Vance River",
    "84" : "Vessigny",
    "85" : "Waddle Village"
}

t9CommsDict = {
    "1"	: "Argyle/Kendal",
    "2"	: "Arnos Vale",
    "3"	: "Bacolet",
    "4"	: "Bagatelle",
    "5"	: "Belle Gardens",
    "6"	: "Belmont",
    "7"	: "Bethel",
    "8"	: "Bethel/Mt. Gomery",
    "9"	: "Bethesda",
    "10" : "Bethlehem",
    "11" : "Betsy\'s Hope",
    "12" : "Black Rock",
    "13" : "Bloody Bay",
    "14" : "Bon Accord",
    "15" : "Buccoo/Coral Gardens",
    "16" : "Calder Hall/Friendsfield",
    "17" : "Campbleton/Charlotteville",
    "18" : "Canaan",
    "19" : "Carnbee/All Field Trace",
    "20" : "Carnbee/All Field Trace",
    "21" : "Carnbee/Patience Hill",
    "22" : "Castara",
    "23" : "Charlotteville",
    "24" : "Cinnamon Hall (Gov\'t House)",
    "25" : "Concordia",
    "26" : "Crown Point",
    "27" : "Culloden",
    "28" : "Darrel Spring",
    "29" : "Delaford",
    "30" : "Delaford/Louis D\'or/Lands",
    "31" : "Easterfield",
    "32" : "Glamorgan",
    "33" : "Golden Lane",
    "34" : "Goodwood",
    "35" : "Hope Farm/John Dial",
    "36" : "Hope/Blenheim",
    "37" : "Idlewild/Whim",
    "38" : "King\'s Bay",
    "39" : "Lambeau",
    "40" : "L\'anse Fourmi",
    "41" : "Les Coteaux",
    "42" : "Lowlands",
    "43" : "Lucy Vale",
    "44" : "Mary\'s Hill",
    "45" : "Mason Hall",
    "46" : "Milford Court/Pigeon Point",
    "47" : "Moriah",
    "48" : "Mount Grace",
    "49" : "Mount Marie",
    "50" : "Mount St. George",
    "51" : "Mt. Irvine/Black Rock",
    "52" : "Old Grange/Sou Sou Lands",
    "53" : "Orange Hill",
    "54" : "Parlatuvier",
    "55" : "Patience Hill",
    "56" : "Pembroke",
    "57" : "Plymouth",
    "58" : "Roxborough",
    "59" : "Sargeant Cain",
    "60" : "Scarborough",
    "61" : "Sherwood Park",
    "62" : "Signal Hill/Patience Hill",
    "63" : "Speyside",
    "64" : "Spring Garden/Signal Hill",
    "65" : "Top Hill",
    "66" : "Whim",
    "67" : "Zion Hill"
}

t1Municipal = {
    "1"	: "Diego Martin",
    "2"	: "Port of Spain",
    "3"	: "San Juan/ Laventille"
}

t2Municipal = {
    "1"	: "Diego Martin",
    "2"	: "San Juan/ Laventille",
    "3"	: "Tunapuna/ Piarco"
}

t3Municipal = {
    "1"	: "Arima",
    "2" : "Couva/ Tabaquite/ Talparo",
    "3" : "San Juan / Laventille",
    "4" : "Sangre Grande",
    "5" : "Tunapuna/ Piarco"
}

t4Municipal = {
    "1" : "Couva/ Tabaquite/ Talparo",
    "2" : "Rio Claro/ Mayaro",
    "3" : "Sangre Grande"
}

t5Municipal = {
    "1"	: "Chaguanas",
    "2"	: "Couva/ Tabaquite/ Talparo",
    "3"	: "San Juan / Laventille",
    "4"	: "Tunapuna/ Piarco"
}

t6Municipal = {
    "1" : "Couva/ Tabaquite/ Talparo",
    "2" : "Princes Town",
    "3" : "Rio Claro/ Mayaro",
    "4" : "Sangre Grande"
}

t7Municipal = {
    "1" : "Couva/ Tabaquite/ Talparo",
    "2" : "Penal/ Debe",
    "3" : "Princes Town",
    "4" : "Rio Claro/ Mayaro",
    "5" : "San Fernando"
}

t8Municipal = {
    "1"	: "Penal/ Debe",
    "2" : "Point Fortin",
    "3" : "Princes Town",
    "4" : "Siparia"
}

t9Municipal = {
    "1" : "Tobago"
}

subtypeDict = {
    "1" : "T1",
    "2" : "T2",
    "3" : "T3",
    "4" : "T4",
    "5" : "T5",
    "6" : "T6",
    "7" : "T7",
    "8" : "T8",
    "9" : "T9"
}

# Use list to add fields and calculate XY
for fc in fcList:
    arcpy.management.AddFields(
    fc,
    [['PlanningRegionCode', 'SHORT', 'Planning Region Code']])
    
    calFields = ["PlanningRegion", "PlanningRegionCode"]
    
    # Check the planning region for each record and update with corresponding code
    with arcpy.da.UpdateCursor(fc, calFields) as calcursor:
        for row in calcursor:
            if row[0] == 'T1':
                row[1] = 1
            elif row[0] == 'T2':
                row[1] = 2
            elif row[0] == 'T3':
                row[1] = 3
            elif row[0] == 'T4':
                row[1] = 4
            elif row[0] == 'T5':
                row[1] = 5
            elif row[0] == 'T6':
                row[1] = 6
            elif row[0] == 'T7':
                row[1] = 7
            elif row[0] == 'T8':
                row[1] = 8
            else:
                row[1] = 9

            calcursor.updateRow(row)

            arcpy.AddMessage("Region codes updated for {0}.".format(fc))     
try:
    for fc in fcList:
        # Set subtype on Planning Region Code field
        arcpy.SetSubtypeField_management(fc, "PlanningRegionCode")
        
        arcpy.AddMessage("Subtype set for {0}.".format(fc))

        # Add subtypes
        for code in subtypeDict:
            arcpy.AddSubtype_management(fc, code, subtypeDict[code])
            
            arcpy.AddMessage("Subtypes added {0}.".format(fc))
        
except:
    arcpy.AddMessage("Subtype could not created for {0}.".format(fc))
    
try:
    # Create T1 Communities domain
    arcpy.CreateDomain_management(inGDB, "T1Communities", "Valid T1 communities", "TEXT", "CODED")
    t1CommsDomain = "T1Communities"
    # Add values from T1 Comms dict to domain
    for code in t1CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t1CommsDomain, code, t1CommsDict[code])

    arcpy.AddMessage("T1 Communities domain created.")

except:
    arcpy.AddMessage("T1 Communities domain was not created.")

try:
    # Create T2 Communities domain
    arcpy.CreateDomain_management(inGDB, "T2Communities", "Valid T2 communities", "TEXT", "CODED")
    t2CommsDomain = "T2Communities"
    # Add values from T2 Comms dict to domain
    for code in t2CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t2CommsDomain, code, t2CommsDict[code])

    arcpy.AddMessage("T2 Communities domain created.")

except:
    arcpy.AddMessage("T2 Communities domain was not created.")

try:
    # Create T3 Communities domain
    arcpy.CreateDomain_management(inGDB, "T3Communities", "Valid T3 communities", "TEXT", "CODED")
    t3CommsDomain = "T3Communities"
    # Add values from T3 Comms dict to domain
    for code in t3CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t3CommsDomain, code, t3CommsDict[code])

    arcpy.AddMessage("T3 Communities domain created.")

except:
    arcpy.AddMessage("T3 Communities domain was not created.")

try:
    # Create T4 Communities domain
    arcpy.CreateDomain_management(inGDB, "T4Communities", "Valid T4 communities", "TEXT", "CODED")
    t4CommsDomain = "T4Communities"
    # Add values from T4 Comms dict to domain
    for code in t4CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t4CommsDomain, code, t4CommsDict[code])

    arcpy.AddMessage("T4 Communities domain created.")

except:
    arcpy.AddMessage("T4 Communities domain was not created.")

try:
    # Create T5 Communities domain
    arcpy.CreateDomain_management(inGDB, "T5Communities", "Valid T5 communities", "TEXT", "CODED")
    t5CommsDomain = "T5Communities"
    # Add values from T5 Comms dict to domain
    for code in t5CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t5CommsDomain, code, t5CommsDict[code])

    arcpy.AddMessage("T5 Communities domain created.")

except:
    arcpy.AddMessage("T5 Communities domain was not created.")

try:
    # Create T6 Communities domain
    arcpy.CreateDomain_management(inGDB, "T6Communities", "Valid T6 communities", "TEXT", "CODED")
    t6CommsDomain = "T6Communities"
    # Add values from T6 Comms dict to domain
    for code in t6CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t6CommsDomain, code, t6CommsDict[code])

    arcpy.AddMessage("T6 Communities domain created.")

except:
    arcpy.AddMessage("T6 Communities domain was not created.")

try:
    # Create T7 Communities domain
    arcpy.CreateDomain_management(inGDB, "T7Communities", "Valid T7 communities", "TEXT", "CODED")
    t7CommsDomain = "T7Communities"
    # Add values from T7 Comms dict to domain
    for code in t7CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t7CommsDomain, code, t7CommsDict[code])

    arcpy.AddMessage("T7 Communities domain created.")

except:
    arcpy.AddMessage("T7 Communities domain was not created.")

try:
    # Create T8 Communities domain
    arcpy.CreateDomain_management(inGDB, "T8Communities", "Valid T8 communities", "TEXT", "CODED")
    t8CommsDomain = "T8Communities"
    # Add values from T8 Comms dict to domain
    for code in t8CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t8CommsDomain, code, t8CommsDict[code])

    arcpy.AddMessage("T8 Communities domain created.")

except:
    arcpy.AddMessage("T8 Communities domain was not created.")

try:
    # Create T9 Communities domain
    arcpy.CreateDomain_management(inGDB, "T9Communities", "Valid T9 communities", "TEXT", "CODED")
    t9CommsDomain = "T9Communities"
    # Add values from T9 Comms dict to domain
    for code in t9CommsDict:
        arcpy.AddCodedValueToDomain_management(inGDB, t9CommsDomain, code, t9CommsDict[code])

    arcpy.AddMessage("T9 Communities domain created.")

except:
    arcpy.AddMessage("T9 Communities domain was not created.")

try:
    # Create T1 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T1MunicipalAreas", "Valid T1 municipal areas", "TEXT", "CODED")
    t1MunicipalDomain = "T1MunicipalAreas"
    # Add values from T1 Municipal dict to domain
    for code in t1Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t1MunicipalDomain, code, t1Municipal[code])

    arcpy.AddMessage("T1 municipal areas domain created.")

except:
    arcpy.AddMessage("T1 municipal areas domain was not created.")

try:
    # Create T2 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T2MunicipalAreas", "Valid T2 municipal areas", "TEXT", "CODED")
    t2MunicipalDomain = "T2MunicipalAreas"
    # Add values from T2 Municipal dict to domain
    for code in t2Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t2MunicipalDomain, code, t2Municipal[code])

    arcpy.AddMessage("T2 municipal areas domain created.")

except:
    arcpy.AddMessage("T2 municipal areas domain was not created.")

try:
    # Create T3 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T3MunicipalAreas", "Valid T3 municipal areas", "TEXT", "CODED")
    t3MunicipalDomain = "T3MunicipalAreas"
    # Add values from T3 Municipal dict to domain
    for code in t3Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t3MunicipalDomain, code, t3Municipal[code])

    arcpy.AddMessage("T3 municipal areas domain created.")

except:
    arcpy.AddMessage("T3 municipal areas domain was not created.")

try:
    # Create T4 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T4MunicipalAreas", "Valid T4 municipal areas", "TEXT", "CODED")
    t4MunicipalDomain = "T4MunicipalAreas"
    # Add values from T4 Municipal dict to domain
    for code in t4Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t4MunicipalDomain, code, t4Municipal[code])

    arcpy.AddMessage("T4 municipal areas domain created.")

except:
    arcpy.AddMessage("T4 municipal areas domain was not created.")

try:
    # Create T5 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T5MunicipalAreas", "Valid T5 municipal areas", "TEXT", "CODED")
    t5MunicipalDomain = "T5MunicipalAreas"
    # Add values from T5 Municipal dict to domain
    for code in t5Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t5MunicipalDomain, code, t5Municipal[code])

    arcpy.AddMessage("T5 municipal areas domain created.")

except:
    arcpy.AddMessage("T5 municipal areas domain was not created.")

try:
    # Create T6 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T6MunicipalAreas", "Valid T6 municipal areas", "TEXT", "CODED")
    t6MunicipalDomain = "T6MunicipalAreas"
    # Add values from T6 Municipal dict to domain
    for code in t6Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t6MunicipalDomain, code, t6Municipal[code])

    arcpy.AddMessage("T6 municipal areas domain created.")

except:
    arcpy.AddMessage("T6 municipal areas domain was not created.")

try:
    # Create T7 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T7MunicipalAreas", "Valid T7 municipal areas", "TEXT", "CODED")
    t7MunicipalDomain = "T6MunicipalAreas"
    # Add values from T7 Municipal dict to domain
    for code in t7Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t7MunicipalDomain, code, t7Municipal[code])

    arcpy.AddMessage("T7 municipal areas domain created.")

except:
    arcpy.AddMessage("T7 municipal areas domain was not created.")

try:
    # Create T8 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T8MunicipalAreas", "Valid T8 municipal areas", "TEXT", "CODED")
    t8MunicipalDomain = "T8MunicipalAreas"
    # Add values from T8 Municipal dict to domain
    for code in t8Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t8MunicipalDomain, code, t8Municipal[code])

    arcpy.AddMessage("T8 municipal areas domain created.")

except:
    arcpy.AddMessage("T8 municipal areas domain was not created.")

try:
    # Create T9 Municipal Areas domain
    arcpy.CreateDomain_management(inGDB, "T9MunicipalAreas", "Valid T9 municipal areas", "TEXT", "CODED")
    t9MunicipalDomain = "T9MunicipalAreas"
    # Add values from T9 Municipal dict to domain
    for code in t9Municipal:
        arcpy.AddCodedValueToDomain_management(inGDB, t9MunicipalDomain, code, t9Municipal[code])

    arcpy.AddMessage("T9 municipal areas domain created.")

except:
    arcpy.AddMessage("T9 municipal areas domain was not created.")

try:
    for fc in fcList:
        # Assign community domains to commnity field and associated subtypes
        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t1CommsDomain, "1: T1")
        
        arcpy.AddMessage("T1 Domian applied to community field.")

        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t2CommsDomain, "2: T2")
        
        arcpy.AddMessage("T2 Domian applied to community field.")

        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t3CommsDomain, "3: T3")
        
        arcpy.AddMessage("T3 Domian applied to community field.")
        
        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t4CommsDomain, "4: T4")
        
        arcpy.AddMessage("T4 Domian applied to community field.")
        
        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t5CommsDomain, "5: T5")
        
        arcpy.AddMessage("T5 Domian applied to community field.")
        
        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t6CommsDomain, "6: T6")
        
        arcpy.AddMessage("T6 Domian applied to community field.")
        
        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t7CommsDomain, "7: T7")
        
        arcpy.AddMessage("T7 Domian applied to community field.")
        
        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t8CommsDomain, "8: T8")
        
        arcpy.AddMessage("T8 Domian applied to community field.")
        
        arcpy.AssignDomainToField_management(fc, "CommunityDistrict", t9CommsDomain, "9: T9")
        
        arcpy.AddMessage("T9 Domian applied to community field.")
        
        # Assign area domains to area municipal field and associated subtypes
        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t1MunicipalDomain, "1: T1")
        
        arcpy.AddMessage("Area municipal T1 domian applied to area field.")
        
        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t2MunicipalDomain, "2: T2")
        
        arcpy.AddMessage("Area municipal T2 domian applied to area field.")

        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t3MunicipalDomain, "3: T3")
        
        arcpy.AddMessage("Area municipal T3 domian applied to area field.")

        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t4MunicipalDomain, "4: T4")
        
        arcpy.AddMessage("Area municipal T4 domian applied to area field.")
        
        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t5MunicipalDomain, "5: T5")
        
        arcpy.AddMessage("Area municipal T5 domian applied to area field.")
        
        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t6MunicipalDomain, "6: T6")
        
        arcpy.AddMessage("Area municipal T6 domian applied to area field.")
        
        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t7MunicipalDomain, "7: T7")
        
        arcpy.AddMessage("Area municipal T7 domian applied to area field.")
        
        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t8MunicipalDomain, "8: T8")
        
        arcpy.AddMessage("Area municipal T8 domian applied to area field.")
        
        arcpy.AssignDomainToField_management(fc, "AreaMunicipal", t9MunicipalDomain, "9: T9")
        
        arcpy.AddMessage("Area municipal T9 domian applied to area field.")
except:
    arcpy.AddMessage("Domain was not assigned to field in {0}.".format(fc))