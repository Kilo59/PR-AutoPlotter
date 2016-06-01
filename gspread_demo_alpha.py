'''
Guilford College
Summer 16
Goal: Demonstration of gspread api to read data from a Google Spreadsheet, manipulate it in Python and write it back to the Spreadsheet
Stretch Goal: Multiple computational examples (Biology relavant), calculate compute time (append to Gsheet)
'''
import gspread  #api to interface with Google Sheets
from oauth2client.service_account import ServiceAccountCredentials #to authorize GAPP access
import RunTime #to calculate script run-time
import demoFunc #various computational functions

start_time = RunTime.currentTime()#Store script start-time

    ##Recieve GoogleApp authorization from JSON file stored in directory##
JSONfilename = 'dummyAuthorization.json' #must match JSON filename
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSONfilename, scope)
gc = gspread.authorize(credentials)
'''
*IMPORTANT STEP: SpreadSheet must be shared(edit perm.) with the 'client_email' within the JSONfile in this case,
'client_email' = client_email@appspot.gserviceaccount.com
'''

    ##Select Google Spreadsheet/Worksheet and create Worksheets##

##open spreadsheet by 'title', api supports alternates methods via URL, etc.
g_sheet = gc.open("your_Gsheet_Name") #Google Sheet filename

##create worksheet for storing computed data with 51 rows and 4 columns
if g_sheet.get_worksheet(1) == None: #2nd worksheet(@index=1) doesn't exist, create it
    g_sheet.add_worksheet('computed', 51, 4)

#set up variables for selecting worksheets
computed_ws = g_sheet.worksheet('computed') #select computed worksheet by 'title'
data_ws = g_sheet.get_worksheet(0) #select Data worksheet by index

'''
cell_list = data_ws.range('E1:E25')
for cell in cell_list:
    cell.value = 'Done'
'''
data_ws.update_cells(cell_list)
    ##Read Data from spreadsheet##
#NotUsed*dataDictionary = data_ws.get_all_records(empty2zero=False, head=1)#store all spreadsheet data in dictionary, ignore empty cells*

#determine data scope
number_of_columns = data_ws.col_count

#store data as lists
colA = (data_ws.col_values(1))
colB = (data_ws.col_values(2))
colC = (data_ws.col_values(3))
colD = (data_ws.col_values(4))

#remove and store column headers
colA_header = colA.pop(0)
colB_header = colB.pop(0)
colC_header = colC.pop(0)
colD_header = colD.pop(0)

#remove empty values
for i in range(len(colA)):
    if colA.count('') > 0:
        del colA[colA.index('')]

for i in range(len(colB)):
    if colB.count('') > 0:
        del colB[colB.index('')]

for i in range(len(colC)):
    if colC.count('') > 0:
        del colC[colC.index('')]

for i in range(len(colD)):
    if colD.count('') > 0:
        del colD[colD.index('')]

#convert string values to integers for colA
colA = [int(i) for i in colA]

    ##Compute Data##
OnlyBioinformatic = False #Set 'True' to skip non-Bioinformatic, shorten runTime
        ##Integer/Numerical Data
colA_max_value = max(colA)
colA_min_value = min(colA)
colA_average = (sum(colA))/(len(colA))
colA_variance = demoFunc.variance(colA, colA_average)
colA_std_d = demoFunc.std_dev(colA_variance)
        ##Sort Data##
colA_sort_min_max = sorted(colA) #sort list in ascending order
        ##String/Pattern Functions##
#remove duplicates
colA_no_duplicates = demoFunc.remove_duplicates(colA_sort_min_max)
colB_no_duplicates = demoFunc.remove_duplicates(colB)
#count distinct items
colA_distinct_items = demoFunc.distinct_items(colA)
colB_distinct_items = demoFunc.distinct_items(colB)

        ##Bioinformatic Functions
    #read from file according to colC, append .txt, store as string
Genome1 = demoFunc.read_text(colC[0]) #Genome1
#Genome2 = demoFunc.read_text(colC[1]) #Genome2
    #find matches in GenomeString for eachGenome for items in colD
pattern_match_list = []
for genome in colC: #incomplete
    for pattern in colD: #pattern match on the sequence and reverseComplement of sequence
        pattern_match = 0
        pattern_match += demoFunc.PatternCount(pattern, demoFunc.read_text(genome))
        pattern_match += demoFunc.PatternCount(demoFunc.ReverseComplement(pattern) , demoFunc.read_text(genome))
        pattern_match_list.append(pattern_match)

    ##print(data to console)
print('Number of columns:' + str(number_of_columns))

print(colA_header, 'length:', len(colA))
print('Distinct items:', colA_distinct_items)
print(colA)
print(colA_sort_min_max)
print('No Duplicates:', colA_no_duplicates)
print('Average:', colA_average)
print('Variance:', colA_variance)
print('Standard Dev:', colA_std_d)

print(colB_header, 'length:', len(colB))
print('Distinct items:', colB_distinct_items)
print(colB)
print('No Duplicates:', colB_no_duplicates)
# print(pattern, 'count:', colB_pattern_count)
print(colC_header, 'length', len(colC))
print(colC)

print(colD_header, 'length', len(colD))
print(colD)
print(pattern_match_list)

proccess_end_time = RunTime.currentTime()#Store script process_end_time
process_runTime = RunTime.calc_runTime(start_time, proccess_end_time)

print('*Data Proccessing Finished*')
print(str(process_runTime) + 'seconds')

    ##Write Data back to spreadsheet##
#template: computed_ws.update_cell(row, col, 'string')
#Write Column Headers
headerRow = 1
if OnlyBioinformatic == False:
    computed_ws.update_cell(headerRow, 1, 'Num:NoDuplc.')
    computed_ws.update_cell(headerRow, 2, 'String:NoDuplc.')
    #computed_ws.update_cell(headerRow, 3, 'TBD')
    #computed_ws.update_cell(headerRow, 4, 'Validation Fail')
computed_ws.update_cell(headerRow, 3, colC[0]) #Genome1
computed_ws.update_cell(headerRow, 4, 'Matches')
#computed_ws.update_cell(headerRow, 7, colC[1]) #Genome2
#computed_ws.update_cell(headerRow, 8, 'Matches')

#colA no duplicates, ascending order
if OnlyBioinformatic == False:
    for i in range(len(colA_no_duplicates)):
        computed_ws.update_cell(i+2, 1, colA_no_duplicates[i])
    #colB no duplicates
    for i in range(len(colB_no_duplicates)):
        computed_ws.update_cell(i+2, 2, colB_no_duplicates[i])

#write Genome pattern with number of matches in adjacent colum
for i in range(len(pattern_match_list)):
    if i <= len(pattern_match_list):
        computed_ws.update_cell(i+2, 3, colD[i])
        computed_ws.update_cell(i+2, 4, pattern_match_list[i])

# Store script end-time
end_time = RunTime.currentTime()
#data write time
data_write_time = RunTime.calc_runTime(proccess_end_time, end_time)
#total script runtime
runTime = RunTime.calc_runTime(start_time, end_time)

print('**Data Write Finished**')
print(str(data_write_time) + 'seconds')

print('***Finished***')
print(str(runTime) + 'seconds')
