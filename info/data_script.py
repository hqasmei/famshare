import xlrd 
import random
import string
import json
from person import Person

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

##############################################################
# Create an Excel file that contains all the infomation about 
# all the birthdays
direc = "path_to_where_your_xlsx_file"
loc  = (direc) 
###############################################################

wb    = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

rows = sheet.nrows
cols = sheet.ncols

arr = []
 
for i in range(1,rows):  
	if (sheet.cell_value(i, 2)!="" and sheet.cell_value(i, 3)!=""):
		firstName  = sheet.cell_value(i, 2)
		lastName   = sheet.cell_value(i, 3)
		birthDay   = sheet.cell_value(i, 16) 
		birthMonth = sheet.cell_value(i, 15)
		birthYear  = sheet.cell_value(i, 14) 
		arr.append(Person(firstName, lastName, birthDay, birthMonth, birthYear))

data = {}
for j in range(len(arr)):
	data[randomString()] = {
							'firstName' : arr[j].firstName,
							'lastName'  : arr[j].lastName,
							'birthDay'  : arr[j].birthDay,
							'birthMonth': arr[j].birthMonth,
							'birthYear' : arr[j].birthYear,
							} 

# Creates a JSON file that will then be imported to Google Firebase Realtime database
with open('people.json', 'w') as json_file:
  json.dump(data, json_file)