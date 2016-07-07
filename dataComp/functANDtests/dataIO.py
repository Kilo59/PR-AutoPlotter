#dataIO
import csv
import gspread
############Remote Input/Output#######

####Google Sheets authorization
##INCOMPLETE!##
'''
class Google_Sheet(object):
    auth_filename = 'Authorization.json'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_filename, scope)
    gc = gspread.authorize(credentials)
    def __init__(self, spreadsheet, worksheet1):
        self.spreadsheet = spreadsheet
        self.worksheet1 = worksheet1

    def work_sheet(self):
        g_sheet = gc.open(self.spreadsheet)
        ws1 = g_sheet.worksheet(self.worksheet1)
        return ws1

    def count_columns():
        number_of_columns = work_sheet.col_count
        return number_of_columns
'''
##INCOMPLETE!##

#############Local Input/Output######

###CSV info gathering

#modified from jamylak @StackOverflow
def count_rows_CSV(string_filename):
    with open(string_filename,"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)
    return row_count

#modified from mgilson @StackOverflow
def count_columns_CSV(string_filename):
    d = ','
    f=open(string_filename,'r')

    reader0=csv.reader(f,delimiter=d)
    ncol=len(next(reader0)) # Read first line and count columns
    return ncol

def count_rowsXcols(string_filename):
    result = count_columns_CSV(string_filename) * count_rows_CSV(string_filename)
    return result

####CSV input
def firstRow_CSV_reader(string_filename):
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        row_1_list = reader1.__next__()
    return row_1_list

#not funtional
'''
def singleCol_CSV_reader(string_filename):
    csv_as_list = []
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in reader1:
            csv_as_list.append(i)
    return csv_as_list
'''
def skipRows_CSV_reader(string_filename, num_skiped_rows):
    csv_as_list = []
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for number in range(1, num_skiped_rows + 1):
            next(reader1)
        for i in reader1:
            csv_as_list.append(i)
    return csv_as_list

def readAll_CSV_reader(string_filename):
    csv_as_list = []
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in reader1:
            csv_as_list.append(i)
    return csv_as_list

def csv_list_of_lists(string_filename):
    headers = firstRow_CSV_reader(string_filename)
    with open(string_filename) as csvfile:
        reader3 = csv.DictReader(csvfile)
        list1 = [[] for x in range(len(headers))]
        for ls, header in zip(list1, headers):
            ls.append(header)
        for row in reader3:
            #print(row['Time'], row['Well 101'], row['Well 300'])
            for col_list in list1:
                col_list.append(row[col_list[0]])
    return list1

####CSV Output
def singleCol_CSV(string_filename, string_header, item_list):
    with open(string_filename, 'w', newline='') as csvfile:
        writer1 = csv.writer(csvfile, delimiter= ',')
        writer1.writerow([string_header])
        for i in range(len(item_list)):
            writer1.writerow([item_list[i]])
    return


#Columns must be past be passed in as a list of lists, each with the same length
def doubleCol_CSV(filename, header_list, list_of_columns):
    with open(filename, 'w', newline='') as csvfile:
        writer2 = csv.writer(csvfile, delimiter=',')
        if len(list_of_columns[0]) != len(list_of_columns[1]):
            print("ERROR: Columns must have the same number of items")
            writer2.writerow( ['ERROR: Columns must have the same number of items'] )
        else:
            writer2.writerow([header_list[0], header_list[1]])
            for i in range(len(list_of_columns[0])):
                writer2.writerow([ list_of_columns[0][i],list_of_columns[1][i] ])
    return

##########|Misc|#################

def csv_dialect():
    print(csv.list_dialects)
    return

def print_data_lists(list_of_lists):
    for i in range(len(list_of_lists)):
        print(list_of_lists[i][0], list_of_lists[i][1:])
    return
