##---------------Loading libraries -------------------------------------------##
import csv
import xlsxwriter

##---------------Functions ---------------------------------------------------##

# inladen csv

with open('gemeente_CDA_data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=';', quotechar='|')
	
	# Create an new Excel file and add a worksheet.
	workbook = xlsxwriter.Workbook('codes.xlsx')
	worksheet = workbook.add_worksheet("Stemmen_per_gemeente")

	list_dicts = []

	for row in reader:
		list_dicts.append(row)

	# creates empty time table
	col = 0
	line = 0

	worksheet.write(0, col, "50Plus")
	col += 1
	worksheet.write(0, col, "score")
	col -= 1
	line += 1
	print(list_dicts)

	for i in range(2, len(list_dicts)):
		buffer_it =(list_dicts[i][0])
		bewerkt = buffer_it[2:]
		plaats = list_dicts[i][1]
		worksheet.write(line, col, bewerkt)
		worksheet.write(line, (col+1), plaats)
		line += 1
	workbook.close()