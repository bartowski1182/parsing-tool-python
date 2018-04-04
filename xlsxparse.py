# -*- coding: utf-8 -*-
import xlsxwriter
import datetime
import xlrd
import re

EVENT_CATEGORY_INDEX = 0
EVENT_GROUP_INDEX = 1
EVENT_SUBGROUP_INDEX = 2
EVENT_TYPE_INDEX = 3
PLACE_INDEX = 4
EVENT_START_DATE_INDEX = 5
COMMENT_INDEX = 6
FATALITIES_INDEX = 7
INJURED_INFECTED_INDEX = 8
EVACUATED_INDEX = 9
ESTIMATED_TOTAL_COST_INDEX = 10
NORMALIZED_TOTAL_COST_INDEX = 11
EVENT_END_DATE_INDEX = 12
FEDERAL_DFAA_PAYMENTS_INDEX = 13
PROVINCIAL_DFAA_PAYMENTS = 14
PROVINCIAL_DEPARTMENT_PAYMENTS_INDEX = 15
MUNICIPAL_COSTS_INDEX = 16
OGD_COSTS_INDEX = 17
INSURANCE_PAYMENTS_INDEX = 18
NGO_PAYMENTS_INDEX = 19
UTILITY_PEOPLE_AFFECTED_INDEX = 20
MAGNITUDE_INDEX = 21

startDateKey = 1
endDateKey = 2
disasterKey = 1
descriptionKey = 1
locationKey = 1
costKey = 1
weatherKey = 1
popStatsKey = 1

wbRD = xlrd.open_workbook("./CanadianDisasterDatabase.xlsx")
sheets = wbRD.sheets()

date = open("date.csv", "w")
fact = open("fact.csv", "w")
disaster = open("disaster.csv", "w")
summary = open("summary.csv", "w")
cost = open("cost.csv", "w")
location = open("location.csv", "w")

firstTime = 1
Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [('Winter', (datetime.date(Y,  1,  1),  datetime.date(Y,  3, 20))),
           ('Spring', (datetime.date(Y,  3, 21),  datetime.date(Y,  6, 20))),
           ('Summer', (datetime.date(Y,  6, 21),  datetime.date(Y,  9, 22))),
           ('Autumn', (datetime.date(Y,  9, 23),  datetime.date(Y, 12, 20))),
           ('Winter', (datetime.date(Y, 12, 21),  datetime.date(Y, 12, 31)))]

internationalSeason =   [('Summer', (datetime.date(Y,  1,  1),  datetime.date(Y,  3, 20))),
                         ('Autumn', (datetime.date(Y,  3, 21),  datetime.date(Y,  6, 20))),
                         ('Winter', (datetime.date(Y,  6, 21),  datetime.date(Y,  9, 22))),
                         ('Spring', (datetime.date(Y,  9, 23),  datetime.date(Y, 12, 20))),
                         ('Summer', (datetime.date(Y, 12, 21),  datetime.date(Y, 12, 31)))]


for sheet in sheets:
    for row in range(sheet.nrows):
        if (firstTime == 1):
            firstTime = 0
            continue
        #print(row)

        cities = []

        locationCell = str(sheet.cell(row, PLACE_INDEX).value.encode("utf-8"))
        provinceList = []
        if (row == 32):
            province = "Ontario"
            cities = ["Toronto"]
        elif (locationCell.strip() == "Prairie Provinces" or locationCell.strip() == "Prairies Provinces" or locationCell.strip() == "Southern Prairies" or locationCell.strip() == "Western Prairies"):
            provinceList = ["Alberta", "Manitoba", "Saskatchewan"]
        elif (locationCell.strip() == "Across Canada"):
            provinceList = ["Quebec", "Ontario", "Newfoundland and Labrador", "Yukon", "Nunavut", "Northwest Territories", "British Columbia", "Saskatchewan", "Manitoba", "New Brunswick", "Prince Edward Island", "Nova Scotia", "Alberta"]
        elif (locationCell.strip().lower() == "maritime provinces" or locationCell.strip().lower() == "martime provinces"):
            provinceList = ["Newfoundland and Labrador", "New Brunswick", "Nova Scotia"]
        elif (locationCell.strip().lower() == "eastern canada"):
            provinceList = ["Newfoundland and Labrador", "New Brunswick", "Nova Scotia", "Ontaio", "Prince Edward Island", "Quebec"]
        elif (locationCell.strip() == "Lakes Huron, Erie and Ontario"):
            provinceList = ["Ontario"]
        elif (locationCell.strip() == "Northumberland Strait (NS and PE)"):
            provinceList = ["Nova Scotia", "Prince Edward Island"]
        elif (locationCell.strip() == "Southern Alberta and Saskatchewan" or locationCell.strip() == "Alberta and Saskatchewan"):
            provinceList = ["Alberta", "Saskatchewan"]
        elif (locationCell.strip() == "Prairies Provinces and Ontario"):
            provinceList = ["Ontario", "Alberta", "Manitoba", "Saskatchewan"]
        elif (locationCell.strip() == "Quebec and Ontario"):
            provinceList = ["Ontario", "Quebec"]
        elif (locationCell.strip() == "Across Toronto, Canada, and internationally"):
            provinceList = ["Quebec", "Ontario", "Newfoundland and Labrador", "Yukon", "Nunavut", "Northwest Territories", "British Columbia", "Saskatchewan", "Manitoba", "New Brunswick", "Prince Edward Island", "Nova Scotia", "Alberta"]
        elif (locationCell.strip() == "Western Canada"):
            provinceList = ["British Columbia", "Alberta", "Saskatchewan", "Manitoba"]
        elif (locationCell.strip() == "Across Canada, largely in the Greater Toronto area"):
            provinceList = ["Ontario"]
        elif (locationCell.strip() == "New Brunswick and Nova Scotia"):
            provinceList = ["New Brunswick", "Nova Scotia"]
        elif (locationCell.strip() == "Nova Scotia, Prince Edward Island and Newfoundland"):
            provinceList = ["Nova Scotia", "Prince Edward Island", "Newfoundland"]
        elif (locationCell.strip() == "New Brunswick and Quebec"):
            provinceList = ["New Brunswick", "Quebec"]
        elif (locationCell.strip() == "Yukon, Northwest Territories and British Columbia"):
            provinceList = ["Yukon", "Northwest Territories", "British Columbia"]
        elif (locationCell.strip() == "Fort Albany and Kashcewan First Nation"):
            provinceList = ["Ontario"]
        elif (locationCell.strip() == " Alberta, Saskatchewan, Manitoba and Ontario"):
            provinceList = ["Alberta", "Saskatchewan", "Manitoba", "Ontario"]
        elif (locationCell.strip() == "St. Lawrence River"):
            provinceList = ["Quebec"]
        elif (locationCell.strip() == "St. Lawrence River"):
            provinceList = ["Quebec"]
        elif (locationCell.find("ON") != -1 or locationCell.find("Ontario") != -1):
            province = "Ontario"
            locationCell = locationCell.split("ON")[0]
            locationCell = locationCell.split("Ontario")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Toronto")
        elif (locationCell.find("QC") != -1 or locationCell.find("Quebec") != -1 or locationCell.find("Québec") != -1):
            province = "Quebec"
            locationCell = locationCell.split("QC")[0]
            locationCell = locationCell.split("Quebec")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Quebec")
        elif (locationCell.find("NL") != -1 or locationCell.find("Newfoundland") != -1 or locationCell.find("Labrador") != -1):
            province = "Newfoundland and Labrador"
            locationCell = locationCell.split("NL")[0]
            locationCell = locationCell.split("Newfoundland")[0]
            locationCell = locationCell.split("Labrador")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("St. Johns")
        elif (locationCell.find("PE") != -1 or locationCell.find("Prince Edward") != -1):
            province = "Prince Edward Island"
            locationCell = locationCell.split("PE")[0]
            locationCell = locationCell.split("Prince Edward")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Charlottetown")
        elif (locationCell.find("NS") != -1 or locationCell.find("Nova Scotia") != -1):
            province = "Nova Scotia"
            locationCell = locationCell.split("NS")[0]
            locationCell = locationCell.split("Nova Scotia")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Halifax")
        elif (locationCell.find("NB") != -1 or locationCell.find("New Brunswick") != -1):
            province = "New Brunswick"
            locationCell = locationCell.split("NB")[0]
            locationCell = locationCell.split("New Brunswick")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Moncton")
        elif (locationCell.find("MB") != -1 or locationCell.find("Manitoba") != -1):
            province = "Manitoba"
            locationCell = locationCell.split("MB")[0]
            locationCell = locationCell.split("Manitoba")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Winnipeg")
        elif (locationCell.find("SK") != -1 or locationCell.find("Saskatchewan") != -1):
            province = "Saskatchewan"
            locationCell = locationCell.split("SK")[0]
            locationCell = locationCell.split("Saskatchewan")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Saskatoon")
        elif (locationCell.find("AB") != -1 or locationCell.find("Alberta") != -1):
            province = "Alberta"
            locationCell = locationCell.split("AB")[0]
            locationCell = locationCell.split("Alberta")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Calgary")
        elif (locationCell.find("BC") != -1 or locationCell.find("British Columbia") != -1):
            province = "British Columbia"
            locationCell = locationCell.split("BC")[0]
            locationCell = locationCell.split("British Columbia")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Vancouver")
        elif (locationCell.find("YT") != -1 or locationCell.find("Yukon") != -1):
            province = "Yukon"
            locationCell = locationCell.split("YT")[0]
            locationCell = locationCell.split("Yukon")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Whitehorse")
        elif (locationCell.find("NT") != -1 or locationCell.find("Northwest Territories") != -1):
            province = "Northwest Territories"
            locationCell = locationCell.split("NT")[0]
            locationCell = locationCell.split("Northwest Territories")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Yellowknife")
        elif (locationCell.find("NU") != -1 or locationCell.find("Nunavut") != -1):
            province = "Nunavut"
            locationCell = locationCell.split("NU")[0]
            locationCell = locationCell.split("Nunavut")[0]
            if (len(locationCell.split(" and ")) > 1):
                cities.append(locationCell.split(" and ")[1])
                locationCell = locationCell.split(" and ")[0]
                if (len(locationCell.split(", ")) > 1):
                    cities.extend(locationCell.split(", "))
                else:
                    cities.append(locationCell)
            elif (locationCell.strip() != ""):
                cities.append(locationCell.strip())
            else:
                cities.append("Iqaluit")
        else:
            continue

        if (not cities or cities[0] == "") and not provinceList:
            continue 

        keywordList = []

        comment = str(sheet.cell(row, COMMENT_INDEX).value.encode("utf-8"))

        if(comment.lower().find("homeless") != -1):
            keywordList.append("homeless")
        if(comment.lower().find("died") != -1):
            keywordList.append("died")
        if(comment.lower().find("injured") != -1):
            keywordList.append("injured")
        if(comment.lower().find("lost") != -1):
            keywordList.append("lost")

        keywordList.extend(['','',''])

        keywordString = ''

        for i in range(0,3):
            keywordString = keywordString + '^' + keywordList[i]

        summary.write(str(descriptionKey) + '^' + comment + keywordString + '\n')        

        cost.write(str(costKey) + "^" + str(sheet.cell(row, ESTIMATED_TOTAL_COST_INDEX).value) + "^" + str(sheet.cell(row, NORMALIZED_TOTAL_COST_INDEX).value) + "^" + str(sheet.cell(row, FEDERAL_DFAA_PAYMENTS_INDEX).value) + "^" + str(sheet.cell(row, PROVINCIAL_DFAA_PAYMENTS).value) + "^" + str(sheet.cell(row, INSURANCE_PAYMENTS_INDEX).value) + "^" + str(sheet.cell(row, PROVINCIAL_DEPARTMENT_PAYMENTS_INDEX).value) + "^" + str(sheet.cell(row, MUNICIPAL_COSTS_INDEX).value) + "^" + str(sheet.cell(row, OGD_COSTS_INDEX).value) + "^" + str(sheet.cell(row, NGO_PAYMENTS_INDEX).value) + "\n")

        year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(int(sheet.cell(row, EVENT_START_DATE_INDEX).value), wbRD.datemode)
        startDate = datetime.datetime(year, month, day, hour, minute)

        placeCell = str(sheet.cell(row, PLACE_INDEX).value.encode("utf-8")).lower().strip()

        if (placeCell.find("ottawa") != -1):
            popStatsKey = 2
        elif (placeCell.find("edmonton") != -1):
            popStatsKey = 3
        elif (placeCell.find("calgary") != -1):
            popStatsKey = 4
        elif (placeCell.find("toronto") != -1):
            popStatsKey = 5
        elif (placeCell.find("halifax") != -1):
            popStatsKey = 6
        elif (placeCell.find("burnaby") != -1):
            popStatsKey = 7
        elif (placeCell.find("new westminster") != -1):
            popStatsKey = 8
        elif (placeCell.find("regina") != -1):
            popStatsKey = 9
        elif (placeCell.find("winnipeg") != -1):
            popStatsKey = 10
        elif (placeCell.find("cochrane") != -1):
            popStatsKey = 11
        elif (placeCell.find("fredericton") != -1):
            popStatsKey = 12
        elif (placeCell.find("charlottetown") != -1):
            popStatsKey = 13
        elif (placeCell.find("nanaimo") != -1):
            popStatsKey = 14
        elif (placeCell.find("dartmouth") != -1):
            popStatsKey = 15
        elif (placeCell.find("victoria") != -1):
            popStatsKey = 16
        elif (placeCell.find("woodstock") != -1):
            popStatsKey = 17
        elif (placeCell.find("montreal") != -1):
            popStatsKey = 18
        elif (placeCell.find("westmount") != -1):
            popStatsKey = 19
        elif (placeCell.find("sarnia") != -1):
            popStatsKey = 20
        elif (placeCell.find("lethbridge") != -1):
            popStatsKey = 21
        elif (placeCell.find("taber") != -1):
            popStatsKey = 22
        elif (placeCell.find("saint-basile-le-grand") != -1):
            popStatsKey = 23
        elif (placeCell.find("niagara falls") != -1):
            popStatsKey = 24
        elif (placeCell.find("dryden") != -1):
            popStatsKey = 25
        elif (placeCell.find("banff") != -1):
            popStatsKey = 26
        elif (placeCell.find("red deer") != -1):
            popStatsKey = 27
        elif (placeCell.find("vernon") != -1):
            popStatsKey = 28
        elif (placeCell.find("oakville") != -1):
            popStatsKey = 29
        elif (placeCell.find("yellowknife") != -1):
            popStatsKey = 30
        elif (placeCell.find("st. john's") != -1):
            popStatsKey = 31
        elif (placeCell.find("truro") != -1):
            popStatsKey = 32
        elif (placeCell.find("windsor") != -1):
            popStatsKey = 33
        elif (placeCell.find("kirkland lake") != -1):
            popStatsKey = 34
        elif (placeCell.find("sydney") != -1):
            popStatsKey = 35
        elif (placeCell.find("aylmer") != -1):
            popStatsKey = 36
        elif (placeCell.find("salmon arm") != -1):
            popStatsKey = 37
        elif (placeCell.find("hamilton") != -1):
            popStatsKey = 38
        elif (placeCell.find("grande prairie") != -1):
            popStatsKey = 39
        elif (placeCell.find("timmins") != -1):
            popStatsKey = 40
        elif (placeCell.find("portage la prairie") != -1):
            popStatsKey = 41
        elif (placeCell.find("barrie") != -1):
            popStatsKey = 42
        elif (placeCell.find("terrace") != -1):
            popStatsKey = 43
        elif (placeCell.find("kenora") != -1):
            popStatsKey = 44
        elif (placeCell.find("drummondville") != -1):
            popStatsKey = 45
        elif (placeCell.find("vancouver") != -1):
            popStatsKey = 46
        elif (placeCell.find("fort frances") != -1):
            popStatsKey = 47
        elif (placeCell.find("brantford") != -1):
            popStatsKey = 48
        elif (placeCell.find("cole harbour") != -1):
            popStatsKey = 49
        elif (placeCell.find("the pas") != -1):
            popStatsKey = 50
        elif (placeCell.find("estevan") != -1):
            popStatsKey = 51
        elif (placeCell.find("edmundston") != -1):
            popStatsKey = 52
        elif (placeCell.find("north vancouver") != -1):
            popStatsKey = 53
        elif (placeCell.find("bridgewater") != -1):
            popStatsKey = 54
        elif (placeCell.find("chibougamau") != -1):
            popStatsKey = 55
        elif (placeCell.find("kelowna") != -1):
            popStatsKey = 56
        elif (placeCell.find("stephenville") != -1):
            popStatsKey = 57
        elif (placeCell.find("abbotsford") != -1):
            popStatsKey = 58
        elif (placeCell.find("delta") != -1):
            popStatsKey = 59
        elif (placeCell.find("boisbriand") != -1):
            popStatsKey = 60
        elif (placeCell.find("amherstburg") != -1):
            popStatsKey = 61
        elif (placeCell.find("sainte-anne-des-plaines") != -1):
            popStatsKey = 62
        elif (placeCell.find("maple ridge") != -1):
            popStatsKey = 63
        elif (placeCell.find("selkirk") != -1):
            popStatsKey = 64
        elif (placeCell.find("gatineau") != -1):
            popStatsKey = 65
        elif (placeCell.find("matane") != -1):
            popStatsKey = 66
        elif (placeCell.find("prince george") != -1):
            popStatsKey = 67
        elif (placeCell.find("saint john") != -1):
            popStatsKey = 68
        elif (placeCell.find("belleville") != -1):
            popStatsKey = 69
        elif (placeCell.find("high river") != -1):
            popStatsKey = 70
        elif (placeCell.find("la tuque") != -1):
            popStatsKey = 71
        elif (placeCell.find("kingston") != -1):
            popStatsKey = 72
        elif (placeCell.find("white rock") != -1):
            popStatsKey = 73
        elif (placeCell.find("swift current") != -1):
            popStatsKey = 74
        elif (placeCell.find("st. albert") != -1):
            popStatsKey = 75
        elif (placeCell.find("camrose") != -1):
            popStatsKey = 76
        elif (placeCell.find("kamloops") != -1):
            popStatsKey = 77
        elif (placeCell.find("vaughan") != -1):
            popStatsKey = 78
        elif (placeCell.find("newmarket") != -1):
            popStatsKey = 79
        elif (placeCell.find("notre-dame-des-prairies") != -1):
            popStatsKey = 80
        elif (placeCell.find("alma") != -1):
            popStatsKey = 81
        elif (placeCell.find("baie-saint-paul") != -1):
            popStatsKey = 82
        elif (placeCell.find("miramichi") != -1):
            popStatsKey = 83
        elif (placeCell.find("mont-laurier") != -1):
            popStatsKey = 84
        elif (placeCell.find("steinbach") != -1):
            popStatsKey = 85
        elif (placeCell.find("midland") != -1):
            popStatsKey = 86
        elif (placeCell.find("north battleford") != -1):
            popStatsKey = 87
        elif (placeCell.find("sydney mines") != -1):
            popStatsKey = 88
        elif (placeCell.find("rimouski") != -1):
            popStatsKey = 89
        elif (placeCell.find("chilliwack") != -1):
            popStatsKey = 90
        elif (placeCell.find("summerside") != -1):
            popStatsKey = 91
        elif (placeCell.find("moose jaw") != -1):
            popStatsKey = 92
        elif (placeCell.find("prince rupert") != -1):
            popStatsKey = 93
        elif (placeCell.find("revelstoke") != -1):
            popStatsKey = 94
        elif (placeCell.find("port alberni") != -1):
            popStatsKey = 95
        elif (placeCell.find("baie-comeau") != -1):
            popStatsKey = 96
        elif (placeCell.find("victoriaville") != -1):
            popStatsKey = 97
        elif (placeCell.find("corner brook") != -1):
            popStatsKey = 98
        elif (placeCell.find("cranbrook") != -1):
            popStatsKey = 99
        elif (placeCell.find("moncton") != -1):
            popStatsKey = 100
        elif (placeCell.find("fort mcmurray") != -1):
            popStatsKey = 101
        elif (placeCell.find("glace bay") != -1):
            popStatsKey = 102
        elif (placeCell.find("north york") != -1):
            popStatsKey = 103
        elif (placeCell.find("mississauga") != -1):
            popStatsKey = 104
        elif (placeCell.find("labrador city") != -1):
            popStatsKey = 105
        elif (placeCell.find("orillia") != -1):
            popStatsKey = 106
        elif (placeCell.find("sherbrooke") != -1):
            popStatsKey = 107
        elif (placeCell.find("drayton valley") != -1):
            popStatsKey = 108
        elif (placeCell.find("london") != -1):
            popStatsKey = 109
        elif (placeCell.find("smiths falls") != -1):
            popStatsKey = 110
        elif (placeCell.find("chatham") != -1):
            popStatsKey = 111
        elif (placeCell.find("hinton") != -1):
            popStatsKey = 112
        elif (placeCell.find("slave lake") != -1):
            popStatsKey = 113
        elif (placeCell.find("brandon") != -1):
            popStatsKey = 114
        elif (placeCell.find("weyburn") != -1):
            popStatsKey = 115
        elif (placeCell.find("yarmouth") != -1):
            popStatsKey = 116
        elif (placeCell.find("lacombe") != -1):
            popStatsKey = 117
        elif (placeCell.find("goderich") != -1):
            popStatsKey = 118
        elif (placeCell.find("duncan") != -1):
            popStatsKey = 119
        elif (placeCell.find("thunder bay") != -1):
            popStatsKey = 120
        elif (placeCell.find("burlington") != -1):
            popStatsKey = 121
        elif (placeCell.find("saint-jean-sur-richelieu") != -1):
            popStatsKey = 122
        elif (placeCell.find("west kelowna") != -1):
            popStatsKey = 123
        else:
            popStatsKey = 1

        weekend = "y"
        if(startDate.weekday() < 5):
            weekday = "n"
        tempDate = startDate.replace(year=Y)
        season = (next(season for season, (start, end) in seasons
            if start <= tempDate.date() <= end))
        intSeason = (next(season for season, (start, end) in internationalSeason
            if start <= tempDate.date() <= end))

        date.write(str(startDateKey) + "^" + str(startDate.day) + "^" + startDate.strftime('%B') + "^" + str(startDate.year) + "^" + weekday + "^" + season + "^" + intSeason + "\n")

        year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(int(sheet.cell(row, EVENT_END_DATE_INDEX).value), wbRD.datemode)
        endDate = datetime.datetime(year, month, day, hour, minute)
        weekend = "y"
        if(endDate.weekday() < 5):
            weekday = "n"
        tempDate = endDate.replace(year=Y)
        season = (next(season for season, (start, end) in seasons
            if start <= tempDate.date() <= end))
        intSeason = (next(season for season, (start, end) in internationalSeason
            if start <= tempDate.date() <= end))

        date.write(str(endDateKey) + "^" + str(endDate.day) + "^" + endDate.strftime('%B') + "^" + str(endDate.year) + "^" + weekday + "^" + season + "^" + intSeason + "\n")

        disaster.write(str(disasterKey) + "^" + str(sheet.cell(row, EVENT_TYPE_INDEX).value) + "^" + str(sheet.cell(row, EVENT_SUBGROUP_INDEX).value) + "^" + str(sheet.cell(row, EVENT_GROUP_INDEX).value) + "^" + str(sheet.cell(row, EVENT_CATEGORY_INDEX).value) + "^" + str(sheet.cell(row, EVENT_TYPE_INDEX).value) + "^" + str(sheet.cell(row, MAGNITUDE_INDEX).value) + "^" + str(sheet.cell(row, UTILITY_PEOPLE_AFFECTED_INDEX).value) + "\n")


        for province in provinceList:
            if province == "Quebec":
                city = "Quebec"
            elif province == "Ontario":
                city = "Ottawa"
            elif province == "Newfoundland and Labrador":
                city = "St. Johns"
            elif province == "Yukon":
                city = "Whitehorse"
            elif province == "Nunavut":
                city = "Iqaluit"
            elif province == "Northwest Territories":
                city = "Yellowknife"
            elif province == "British Columbia":
                city = "Vancouver"
            elif province == "Saskatchewan":
                city = "Saskatoon"
            elif province == "Manitoba":
                city = "Winnipeg"
            elif province == "New Brunswick":
                city = "Moncton"
            elif province == "Prince Edward Island":
                city = "Charlottetown"
            elif province == "Nova Scotia":
                city = "Halifax"
            elif province == "Alberta":
                city = "Calgary"
            location.write(str(locationKey) + "^" + city + "^" + province + "^y\n") 
            fact.write(str(startDateKey) + "^" + str(endDateKey) + "^" + str(locationKey) + "^" + str(disasterKey) + "^" + str(descriptionKey) + "^" + str(costKey) + "^" + str(popStatsKey) + "^" + str(weatherKey) + "^" + str(sheet.cell(row, FATALITIES_INDEX).value) + "^" + str(sheet.cell(row, INJURED_INFECTED_INDEX).value) + "^" + str(sheet.cell(row, EVACUATED_INDEX).value) + "\n")
            locationKey = locationKey + 1

        for city in cities:
            location.write(str(locationKey) + "^" + city + "^" + province + "^y\n") 
            fact.write(str(startDateKey) + "^" + str(endDateKey) + "^" + str(locationKey) + "^" + str(disasterKey) + "^" + str(descriptionKey) + "^" + str(costKey) + "^" + str(popStatsKey) + "^" + str(weatherKey) + "^" + str(sheet.cell(row, FATALITIES_INDEX).value) + "^" + str(sheet.cell(row, INJURED_INFECTED_INDEX).value) + "^" + str(sheet.cell(row, EVACUATED_INDEX).value) + "\n")
            locationKey = locationKey + 1
        startDateKey = startDateKey + 2
        endDateKey = endDateKey + 2
        disasterKey = disasterKey + 1
        costKey = costKey + 1
        descriptionKey = descriptionKey + 1
        
fact.close()
date.close()
disaster.close()
cost.close()
location.close()
summary.close()
