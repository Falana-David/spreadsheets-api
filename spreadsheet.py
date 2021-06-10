from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


credentials = ServiceAccountCredentials.from_json_keyfile_name("testsheets-316317-f66644dbb1a0.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) #authenticate the JSON key with gspread
sample_sheet = file.open('Python Test')
ws = sample_sheet.worksheet('Sheet1') 

def next_available_row(ws):
    str_list = list(filter(None, ws.col_values(1)))
    return str(len(str_list)+1)

next_row = next_available_row(ws)


thisdict = {
  "Company": "Fordqq",
  "Date": "09/12/22",
  "Service Provider": "Verizon Mobile",
  "How Many #'s Submitted": 12,
  "Override" : "No",
  "How Many" : 1,
  "Decision" : "No"
}

new_list = [thisdict.get("Company"), thisdict.get("Date"), thisdict.get("Service Provider")
,thisdict.get("How Many #'s Submitted"), thisdict.get("Override")
,thisdict.get("How Many?"),thisdict.get("Decision")]

# Value Of This Should Be 7
#x = len(new_list)
#r = 1000000000

list = ['A','B','C','D','E','F','G']

#Yo boy tryna make a loop that checks if the first element in the first row is NULL
#if it is null then add the appropriate values to the cells



u = 0
k = 1

def next_available_row1(ws, cols_to_sample=2):
  # looks for empty row based on values appearing in 1st N columns
  cols = ws.range(1, 1, ws.row_count, cols_to_sample)
  return max([cell.row for cell in cols if cell.value]) + 1

p = len(ws.get_all_values()) + 1

for x in new_list:
    y = str(list[u]) + str(p)
    ws.update(str(y), new_list[u])
    if u == 7:
        break
    u+=1
    k+=1
    #else:
     #y = str(list[u]) + str(k)
      #  ws.update_acell(str(y), new_list[u])
    
        #u+=1

   


#while val != NULL
 #   val = worksheet.cell(1, 2).value
  #  worksheet.update('B1', 'Bingo!')




#sourceRange = sample_sheet.getRange('A1:G1')
#sourceRange.autoFillToNeighbor(SpreadsheetApp.AutoFillSeries.DEFAULT_SERIES)

#ws.update_acell('B1', 'Gspread !') 