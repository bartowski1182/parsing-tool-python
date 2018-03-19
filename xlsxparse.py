import xlsxwriter
import xlrd

wbRD = xlrd.open_workbook("/home/colin/Downloads/CanadianDisasterDatabase.xlsx")
sheets = wbRD.sheets()

for sheet in sheets:
    for row in range(sheet.nrows):
        print str(sheet.cell(row, 7).value) + "$" + str(sheet.cell(row, 8).value) + "$" + str(sheet.cell(row, 9).value)

    print "sheet"
