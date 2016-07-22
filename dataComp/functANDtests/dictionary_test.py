import dataIO
import RunTime
import gspread
from oauth2client.service_account import ServiceAccountCredentials #to authorize GAPP access

#####|Google Sheet Setup|#####
#Working Sheet Name
google_sheet_name = 'plate_wells'
#Setup GoogleApp Authrization/Credentials
auth_filename = 'Authorization.json'
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_filename, scope)
gc = gspread.authorize(credentials)
##open spreadsheet by 'title'
g_sheet = gc.open(google_sheet_name)
#setup worksheet variables
well_labels = g_sheet.worksheet('well_labels')
print("****************************")
#setup well_data worksheet & well_grouping worksheet objects
well_data = g_sheet.worksheet('well_data')
well_grouping = g_sheet.worksheet('well_grouping')
###############################

####|Grouping Begin|##
#######TESTING DICTIONARY STRUCTURE
group_dict = well_grouping.get_all_records(empty2zero = False, head = 1)

group_list = []

#loop through dictionary of well_grouping worksheet values
#ignore empty groups, append group names of the rest to a list
for d in group_dict:
    for group_name in d:
        #print(group_name, d[group_name])
        if d[group_name] == '':
            pass
            #print("None")
        else:
            if group_name not in group_list:
                group_list.append(group_name)

print("**********")
print(group_list)

group_list = [group_list[x] for x in range(0, len(group_list)) if group_list[x] != 'Excluded']

print(group_list)

grping_file = 'grouping.R'
system_time = RunTime.system_time()

f = open(grping_file, 'w')
f.write("#file: "+grping_file+"\n#Time: "+RunTime.system_time())
f.close()

g1 = well_grouping.col_values(1)
g2 = well_grouping.col_values(2)
g3 = well_grouping.col_values(3)
g4 = well_grouping.col_values(4)
g5 = well_grouping.col_values(5)
g6 = well_grouping.col_values(6)
g7 = well_grouping.col_values(7)
g8 = well_grouping.col_values(8)
g9 = well_grouping.col_values(9)
g10 = well_grouping.col_values(10)

g_list = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]

#cleanup lists
lists = 10
for index, g in enumerate(g_list):
    # remove empty values
    for i in range(len(g)):
        if g.count('') > 0:
            del g[g.index('')]
    if len(g) <= 1:
        del g[g.index(g[0])]
        lists -= 1
g_list = g_list[:lists]
#remove header
for index, ls in enumerate(g_list):
    group_list[index] = ls[0]
    g_list[index] = ls[1:]

print(">")
for g in g_list:
    print(g)

for grp_index, g in enumerate(g_list):
    group_list[grp_index] += ' <- data.frame('

for grp_index, g in enumerate(g_list):
    for ls_item in g:
        group_list[grp_index] += ls_item+', '
    group_list[grp_index] = group_list[grp_index][:len(group_list[grp_index])-2] +")"

print("*****>")

print(">")
for g in group_list:
    print(g)

a = open(grping_file, 'a')
for group in group_list:
    a.write('\n'+group)
a.close()

'''
print(group_dict)
print(group_dict[0])
print(group_dict[1])
print(group_dict[2])
print(group_dict[0]['Group_16'])
print(group_dict[1]['Group_16'])

for i in range(len(group_dict)):
    print(len(group_dict[i]))
    if group_dict[i]['Group_16'] != '':  # if not empty
        print(group_dict[i]['Group_16'])

for i in range(len(group_dict)):
    print(len(group_dict[i]))
    if group_dict[i]['Group_4'] != '':
        print(group_dict[i]['Group_4'])
'''
####|Grouping End|##