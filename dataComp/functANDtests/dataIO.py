#dataIO
from functANDtests import RunTime
#import RunTime #when running tests in functANDtests folder
import csv
import subprocess
import os
from configparser import SafeConfigParser

#############Local Input/Output######

###reading from Config file
parser = SafeConfigParser()
parser.read('config.txt')
#TODO fix errors when run from commandline
def get_tolerance(req_name):
    tolerance = parser.getfloat('tolerance', req_name)
    return tolerance

def get_start_cond_bol(condition_name):
    condition = parser.getboolean('start_conditions', condition_name)
    return condition
#causing error when run from commandline
def get_start_cond(condition_name):
    condition = parser.get('start_conditions', condition_name)
    if  condition.lower() == 'true' or condition.lower() == 'false' or condition == '1' or condition == '0':
        condition = parser.getboolean('start_conditions', condition_name)
        return condition
    else:
        return condition

def get_R_options(r_option_name):
    r_option = parser.getboolean('r_options', r_option_name)
    return r_option

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
    #check that file exists
    if check_file(string_filename) == True:
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
    else:
        return []

def check_file(filename):
    filefound = True
    try:
        fh = open(filename, 'r')
        fh.close()
    except IOError:
        print('**ERROR: CAN\'NT FIND FILE\n***MAKE SURE THE CONFIG SETTINGS MATCH THE EXPECTED FILENAME')
        filefound = False
    except:
        print('**ERROR: UNKNOWN EXCEPTION OCCURED')
        filefound = False
    else:
        print('*FILE', filename, 'FOUND')
        filefound = True
    return filefound

def check_file_silent(filename):
    filefound = True
    try:
        fh = open(filename, 'r')
        fh.close()
    except:
        filefound = False
    else:
        filefound = True
    return filefound

def exit_without_file(filename):
    filefound = check_file_silent(filename)
    if filefound != True: #if check_file_silent recieves exception
        quit()
    return

########|CSV Output|########

#**used in multiCol_CSV function**
#takes a list of lists (where each list repesents a column of data)
#sorts it into to a list of list where each list represents a row
#Example input:     [ [header1, 0.1, 0.10], [header2, 0.2, 0.20] ]
#Example output:    [ [header1, header2], [0.1, 0.2], [0.10, 0.20] ]
def cols_to_rows_list(list_of_columns):
    #lists should have the same length
    list_of_rows = list_n( len(list_of_columns[0]) )
    for index, row in enumerate(list_of_rows):
        for ls_index in range( len(list_of_columns) ):
            #print(index, ls_index)
            row.append(list_of_columns[ls_index][index])
    return list_of_rows

def multiCol_CSV(filename, list_of_columns):
    row_list = cols_to_rows_list(list_of_columns)
    print("***Written to CSV file***")
    with open(filename, 'w', newline='') as csvfile:
        writer1 = csv.writer(csvfile, delimiter=',')
        for index, ls in enumerate(row_list):
            #print(ls)
            writer1.writerow(ls)
    return

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

#####|Misc file output|#####
#TODO write functions to write to file line by line
#writes string to file
def write_line_a(filename, string):
    with open(filename, 'a') as f:
        f.write(string+'\n')
    return
def append_list_of_string(filename, ls):
    for item in ls:
        write_line_a(filename, item)
    return
#take list of group names, create r code for ggplots of each group
def setup_ggploter(list_of_items_to_plot):
    list_of_plots = group_names(list_of_items_to_plot)
    list_of_items = group_items(list_of_items_to_plot)
    ls_of_strings = []
    color = ['black', 'red', 'blue', 'orange', 'green']
    for group_index, group in enumerate(list_of_plots):
        string1 = 'g'+str(group_index+1)+' <- ggplot()+'
        ls_of_strings.append(string1)
        for index, well in enumerate(list_of_items[group_index]):
            string_point = 'geom_point(data = dat1, aes(Time, dat1$'+str(well)+'), color = \''+str(color[index])+'\') +'
            #print(string_point) #test print
            ls_of_strings.append(string_point)
        #setup ggplot labs() function
        string_labs='labs(title = '+str(group)+', x= \'Time\', y = \'Optical Density\') +'
        ls_of_strings.append(string_labs)
        #setup ggplot theme() function
        string_theme='theme( axis.text.x= element_text(angle = 80, size = 7, vjust = 0.5) )\n'
        ls_of_strings.append(string_theme)
        #setup image_name variable *needed for ggsave()
        str_image_name='image_name <- paste(\''+str(group)+'\', \'.png\', sep = \'\')'
        ls_of_strings.append(str_image_name)
        #setup ggplot ggsave() function
        string_ggsave='ggsave(image_name, width = 22, height = 8)\n'
        ls_of_strings.append(string_ggsave)
    return ls_of_strings
def write_ggploter(filename, list_of_items_to_plot):
    write_line_a(filename, '\n\n####ggplots####')
    ls_of_strings = setup_ggploter(list_of_items_to_plot)
    append_list_of_string(filename, ls_of_strings)
    print('*',filename,': ggplots created')
    return
#return group names
def group_names(g_list):
    #cleanup lists
    lists = 10
    for index, g in enumerate(g_list):
        # remove empty values
        for i in range(len(g)):
            if g.count('') > 0:
                del g[g.index('')]
        if len(g) <= 1:
            #del g[g.index(g[0])]
            lists -= 1
    g_list = g_list[:lists]
    group_list = [g_list[x][0] for x in range(0, len(g_list))]
    return group_list
#return list of wells within groups (absent the group_name header)
def group_items(g_list):
    #cleanup lists
    lists = 10
    for index, g in enumerate(g_list):
        # remove empty values
        #print(index, g) #Testing
        for i in range(len(g)):
            if g.count('') > 0:
                del g[g.index('')]
        if len(g) <= 1:
            #print( '*'+str(g) )
            #del g[g.index(g[0])]
            #print('*DELETE')
            lists -= 1
    g_list = g_list[:lists]
    group_list = [g_list[x][0] for x in range(0, len(g_list))]
    #remove header
    for index, ls in enumerate(g_list):
        group_list[index] = ls[0]
        g_list[index] = ls[1:]
    return g_list
#setup list used to create R grouping file
def setup_r_grping(g_list):
    group_list = group_names(g_list)
    g_list = group_items(g_list)
    #setup dataframes for use in R
    dataframe = 'dat1$'
    for grp_index, g in enumerate(g_list):
        group_list[grp_index] += ' <- data.frame('+dataframe+'Time, '
    for grp_index, g in enumerate(g_list):
        for ls_item in g:
            group_list[grp_index] += dataframe+ls_item+', '
        group_list[grp_index] = group_list[grp_index][:len(group_list[grp_index])-2] +")"
    return group_list

def write_r_grping_file(list_of_columns):
    group_list = setup_r_grping(list_of_columns)
    #create file and overwrite old file
    grping_file = 'grouping.R'
    system_time = RunTime.system_time()
    f = open(grping_file, 'w')
    f.write("#file: "+grping_file+"\n#Time: "+RunTime.system_time())
    f.close()
    #open file and append dataframes
    a = open(grping_file, 'a')
    for group in group_list:
        a.write('\n'+group)
    a.close()
    return

#######|Subprocess|######
def exec_script(command, script_name, arg_list):
    #define command and argument
    current_directory = os.getcwd()
    command = command
    script = script_name
    path2script = current_directory + '\\' + script
    #build subprocess command
    cmd = [command, path2script] + arg_list
    print(cmd, "Finished")
    return cmd

#relies on result of exec_script
def exec_script2(command, script_name, arg_list):
    cmd = exec_script(command, script_name, arg_list)
    #check_output will run command and store to result
    x = subprocess.check_output(cmd, universal_newlines=True) #shell=True unecessary?
    return x
##########|Misc|#################

#return an empty list of lists of variable size
def list_n(size_of_list):
    ls = [[] for i in range(size_of_list)]
    return ls

def csv_dialect():
    print(csv.list_dialects)
    return

def print_data_lists(list_of_lists):
    for i in range(len(list_of_lists)):
        print(list_of_lists[i][0], list_of_lists[i][1:])
    return
