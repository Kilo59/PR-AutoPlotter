#TODO is plate_reader.csv created at end of cycle or begining?
import gspread
from functANDtests import dataIO
from functANDtests import dataCowboy
from functANDtests import RunTime
from oauth2client.service_account import ServiceAccountCredentials #to authorize GAPP access
#####|Functions|#####
def gsheet_update(list_of_lists, num_cols):
    ##Setup sheet write_range
    A = well_data.range('A1:A256')
    B = well_data.range('B1:B256')
    C = well_data.range('C1:C256')
    D = well_data.range('D1:D256')
    E = well_data.range('E1:E256')
    F = well_data.range('F1:F256')
    G = well_data.range('G1:G256')
    H = well_data.range('H1:H256')
    I = well_data.range('I1:I256')
    J = well_data.range('J1:J256')
    K = well_data.range('K1:K256')
    L = well_data.range('L1:L256')
    M = well_data.range('M1:M256')
    N = well_data.range('N1:N256')
    O = well_data.range('O1:O256')
    P = well_data.range('P1:P256')
    Q = well_data.range('Q1:Q256')
    R = well_data.range('R1:R256')
    S = well_data.range('S1:S256')
    T = well_data.range('T1:T256')
    U = well_data.range('U1:U256')
    V = well_data.range('V1:V256')
    W = well_data.range('W1:W256')
    X = well_data.range('X1:X256')
    Y = well_data.range('Y1:Y256')
    Z = well_data.range('Z1:Z256')
    AA = well_data.range('AA1:AA256')
    AB = well_data.range('AB1:AB256')
    AC = well_data.range('AC1:AC256')
    AD = well_data.range('AD1:AD256')
    AE = well_data.range('AE1:AE256')
    AF = well_data.range('AF1:AF256')
    AG = well_data.range('AG1:AG256')
    AH = well_data.range('AH1:AH256')
    AI = well_data.range('AI1:AI256')
    AJ = well_data.range('AJ1:AJ256')
    AK = well_data.range('AK1:AK256')
    AL = well_data.range('AL1:AL256')
    AM = well_data.range('AM1:AM256')
    AN = well_data.range('AN1:AN256')
    AO = well_data.range('AO1:AO256')
    AP = well_data.range('AP1:AP256')
    AQ = well_data.range('AQ1:AQ256')
    AR = well_data.range('AR1:AR256')
    AS = well_data.range('AS1:AS256')
    AT = well_data.range('AT1:AT256')
    AU = well_data.range('AU1:AU256')
    AV = well_data.range('AV1:AV256')
    AW = well_data.range('AW1:AW256')
    AX = well_data.range('AX1:AX256')
    AY = well_data.range('AY1:AY256')
    AZ = well_data.range('AZ1:AZ256')
    BA = well_data.range('BA1:BA256')
    BB = well_data.range('BB1:BB256')
    BC = well_data.range('BC1:BC256')
    BD = well_data.range('BD1:BD256')
    BE = well_data.range('BE1:BE256')
    BF = well_data.range('BF1:BF256')
    BG = well_data.range('BG1:BG256')
    BH = well_data.range('BH1:BH256')
    BI = well_data.range('BI1:BI256')
    BJ = well_data.range('BJ1:BJ256')
    BK = well_data.range('BK1:BK256')
    BL = well_data.range('BL1:BL256')
    BM = well_data.range('BM1:BM256')
    BN = well_data.range('BN1:BN256')
    BO = well_data.range('BO1:BO256')
    BP = well_data.range('BP1:BP256')
    BQ = well_data.range('BQ1:BQ256')
    BR = well_data.range('BR1:BR256')
    BS = well_data.range('BS1:BS256')
    BT = well_data.range('BT1:BT256')
    BU = well_data.range('BU1:BU256')
    BV = well_data.range('BV1:BV256')
    BW = well_data.range('BW1:BW256')
    BX = well_data.range('BX1:BX256')
    BY = well_data.range('BY1:BY256')
    BZ = well_data.range('BZ1:BZ256')
    CA = well_data.range('CA1:CA256')
    CB = well_data.range('CB1:CB256')
    CC = well_data.range('CC1:CC256')
    CD = well_data.range('CD1:CD256')
    CE = well_data.range('CE1:CE256')
    CF = well_data.range('CF1:CF256')
    CG = well_data.range('CG1:CG256')
    CH = well_data.range('CH1:CH256')
    CI = well_data.range('CI1:CI256')
    CJ = well_data.range('CJ1:CJ256')
    CK = well_data.range('CK1:CK256')
    CL = well_data.range('CL1:CL256')
    CM = well_data.range('CM1:CM256')
    CN = well_data.range('CN1:CN256')
    CO = well_data.range('CO1:CO256')
    CP = well_data.range('CP1:CP256')
    CQ = well_data.range('CQ1:CQ256')
    CR = well_data.range('CR1:CR256')
    CS = well_data.range('CS1:CS256')
    CT = well_data.range('CT1:CT256')
    CU = well_data.range('CU1:CU256')
    CV = well_data.range('CV1:CV256')
    CW = well_data.range('CW1:CW256')
    CX = well_data.range('CX1:CX256')
    CY = well_data.range('CY1:CY256')
    CZ = well_data.range('CZ1:CZ256')
    DA = well_data.range('DA1:DA256')
    DB = well_data.range('DB1:DB256')
    DC = well_data.range('DC1:DC256')
    DD = well_data.range('DD1:DD256')
    DE = well_data.range('DE1:DE256')
    DF = well_data.range('DF1:DF256')
    DG = well_data.range('DG1:DG256')
    DH = well_data.range('DH1:DH256')
    DI = well_data.range('DI1:DI256')
    DJ = well_data.range('DJ1:DJ256')
    DK = well_data.range('DK1:DK256')
    DL = well_data.range('DL1:DL256')
    DM = well_data.range('DM1:DM256')
    DN = well_data.range('DN1:DN256')
    DO = well_data.range('DO1:DO256')
    DP = well_data.range('DP1:DP256')
    DQ = well_data.range('DQ1:DQ256')
    DR = well_data.range('DR1:DR256')
    DS = well_data.range('DS1:DS256')
    DT = well_data.range('DT1:DT256')
    DU = well_data.range('DU1:DU256')
    DV = well_data.range('DV1:DV256')
    DW = well_data.range('DW1:DW256')
    DX = well_data.range('DX1:DX256')
    DY = well_data.range('DY1:DY256')
    DZ = well_data.range('DZ1:DZ256')
    EA = well_data.range('EA1:EA256')
    EB = well_data.range('EB1:EB256')
    EC = well_data.range('EC1:EC256')
    ED = well_data.range('ED1:ED256')
    EE = well_data.range('EE1:EE256')
    EF = well_data.range('EF1:EF256')
    EG = well_data.range('EG1:EG256')
    EH = well_data.range('EH1:EH256')
    EI = well_data.range('EI1:EI256')
    EJ = well_data.range('EJ1:EJ256')
    EK = well_data.range('EK1:EK256')
    EL = well_data.range('EL1:EL256')
    EM = well_data.range('EM1:EM256')
    EN = well_data.range('EN1:EN256')
    EO = well_data.range('EO1:EO256')
    EP = well_data.range('EP1:EP256')
    EQ = well_data.range('EQ1:EQ256')
    ER = well_data.range('ER1:ER256')
    ES = well_data.range('ES1:ES256')
    ET = well_data.range('ET1:ET256')
    EU = well_data.range('EU1:EU256')
    EV = well_data.range('EV1:EV256')
    EW = well_data.range('EW1:EW256')
    EX = well_data.range('EX1:EX256')
    EY = well_data.range('EY1:EY256')
    EZ = well_data.range('EZ1:EZ256')
    FA = well_data.range('FA1:FA256')
    FB = well_data.range('FB1:FB256')
    FC = well_data.range('FC1:FC256')
    FD = well_data.range('FD1:FD256')
    FE = well_data.range('FE1:FE256')
    FF = well_data.range('FF1:FF256')
    FG = well_data.range('FG1:FG256')
    FH = well_data.range('FH1:FH256')
    FI = well_data.range('FI1:FI256')
    FJ = well_data.range('FJ1:FJ256')
    FK = well_data.range('FK1:FK256')
    FL = well_data.range('FL1:FL256')
    FM = well_data.range('FM1:FM256')
    FN = well_data.range('FN1:FN256')
    FO = well_data.range('FO1:FO256')
    FP = well_data.range('FP1:FP256')
    FQ = well_data.range('FQ1:FQ256')
    FR = well_data.range('FR1:FR256')
    FS = well_data.range('FS1:FS256')
    FT = well_data.range('FT1:FT256')
    FU = well_data.range('FU1:FU256')
    FV = well_data.range('FV1:FV256')
    FW = well_data.range('FW1:FW256')
    FX = well_data.range('FX1:FX256')
    FY = well_data.range('FY1:FY256')
    FZ = well_data.range('FZ1:FZ256')
    GA = well_data.range('GA1:GA256')
    GB = well_data.range('GB1:GB256')
    GC = well_data.range('GC1:GC256')
    GD = well_data.range('GD1:GD256')
    GE = well_data.range('GE1:GE256')
    GF = well_data.range('GF1:GF256')
    GG = well_data.range('GG1:GG256')
    GH = well_data.range('GH1:GH256')
    GI = well_data.range('GI1:GI256')
    GJ = well_data.range('GJ1:GJ256')
    GK = well_data.range('GK1:GK256')
    GL = well_data.range('GL1:GL256')
    GM = well_data.range('GM1:GM256')
    GN = well_data.range('GN1:GN256')
    GO = well_data.range('GO1:GO256')
    GP = well_data.range('GP1:GP256')
    GQ = well_data.range('GQ1:GQ256')
    GR = well_data.range('GR1:GR256')
    GS = well_data.range('GS1:GS256')
    A_GS = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, AA, AB, AC, AD, AE, AF, AG,
            AH, AI, AJ, AK, AL, AM, AN, AO, AP, AQ, AR, AS, AT, AU, AV, AW, AX, AY, AZ, BA, BB, BC, BD, BE, BF, BG, BH,
            BI, BJ, BK, BL, BM, BN, BO, BP, BQ, BR, BS, BT, BU, BV, BW, BX, BY, BZ, CA, CB, CC, CD, CE, CF, CG, CH, CI,
            CJ, CK, CL, CM, CN, CO, CP, CQ, CR, CS, CT, CU, CV, CW, CX, CY, CZ, DA, DB, DC, DD, DE, DF, DG, DH, DI, DJ,
            DK, DL, DM, DN, DO, DP, DQ, DR, DS, DT, DU, DV, DW, DX, DY, DZ, EA, EB, EC, ED, EE, EF, EG, EH, EI, EJ, EK,
            EL, EM, EN, EO, EP, EQ, ER, ES, ET, EU, EV, EW, EX, EY, EZ, FA, FB, FC, FD, FE, FF, FG, FH, FI, FJ, FK, FL,
            FM, FN, FO, FP, FQ, FR, FS, FT, FU, FV, FW, FX, FY, FZ, GA, GB, GC, GD, GE, GF, GG, GH, GI, GJ, GK, GL, GM,
            GN, GO, GP, GQ, GR, GS]

    # iterate through list_of_lists
    print( len(list_of_lists), "Columns to post" )
    for ls_index, (ls, col) in enumerate(zip( list_of_lists, A_GS[:num_cols] )):
        #print('a', ls_index)
        for cell_index, cell in enumerate(col):
            cell.value = ls[cell_index]
    #update google sheet by column
    update_count = 0
    for col in A_GS[:num_cols]: #list slicing to loop correct number of times
        print('Column', update_count, 'posted')
        update_count += 1
        well_data.update_cells(col)
    return
def get_grouping_data():
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
    return g_list
##############|Start|##########
print("dataWrangle1.py")
print("############|START|##########")
full_print = True
#TODO: fix config parser error that occurs when run from the command line, due to path not being explicitly set?
full_sheet_update = dataIO.get_start_cond('post2google')
input_csv = dataIO.get_start_cond('input_filename') #full filename of CSV file stored in working directory
print('Input filename: ', input_csv)
Rsub = dataIO.get_R_options("execute_r")
#data must be greater than these values to pass validation
#Set = 0 to accept all data
RangeReq = dataIO.get_tolerance('rangeReq')
MaxReq = dataIO.get_tolerance('maxReq')
print('Tolerance: data will be ignored if it does not exceed these requirements')
print('Range Requirement:', RangeReq)
print('Max Value Requirement:', MaxReq)
start_time = RunTime.currentTime()#start-time
Remove_invalid_data = True
grouping = True
generate_r_grping_file = dataIO.get_R_options("gen_grping_file")
print("Remove Invalid Data: ", Remove_invalid_data)
print("R subprocess: ", Rsub)
print("Group Data: ", grouping)
print("Generate grouping.R file: ", generate_r_grping_file)
print("Update Google Sheet: ", full_sheet_update)
start = dataIO.get_start_cond('run')
if start == False:
    print("**config.txt has \'run\' set to \'False\'**")
    print("***STOPPING PROGRAM***")
    quit()
else:
    print('**proceeding with Script**')

##########Get Raw Data-set from Bioscreen CSV file############################
if dataIO.check_file_silent(input_csv) == True:
	original_csv_list_of_lists = dataIO.csv_list_of_lists(input_csv) #store data-set by columns as a list of lists
else:
	dataIO.check_file(input_csv)
	quit()
number_of_rows_csv = dataIO.count_rows_CSV(input_csv)
number_of_cols_csv = dataIO.count_columns_CSV(input_csv)
##############################################################################

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
print(well_labels.title)
###############################

#######Get Well Labels from Google Sheet######################################
labels = dataCowboy.pl_rdr_single_list(well_labels.get_all_values())
#use gspread to collect every cell value in well_wabels workseet, use dataCowboy to store values into a single list of 200 well labels
##############################################################################

#####Replace Headers#####
updated_lists = dataCowboy.header_replacement(original_csv_list_of_lists, labels)
###################|Data Validation|####################

########|Python Summary Data|##########
#print summary data for every column, skip item 0 (the header)
print("###|Summary Data|###")
print("#        Range  | Min   Max      Mean   |        First Last    Name")
count = 1
range_list = [0]
min_list = [0]
max_list = [0]
mean_list = [0]
pass_fail = ''
for index, ls in enumerate(updated_lists[1:]):
    range_val = round(float(max(ls[1:])) - float(min(ls[1:])), 3)
    min_val = min(ls[1:])
    max_val = max(ls[1:])
    mean = round( dataCowboy.list_mean(ls[1:]), 3 )
    first = ls[1]
    last = ls[len(ls)-1]
    #store summary data in seperate lists for later use in data validation/checking
    range_list.append(float(range_val))
    min_list.append(float(min_val))
    max_list.append(float(max_val))
    mean_list.append(float(mean))

    if range_list[index+1] > RangeReq or max_list[index+1] > MaxReq:
        pass_fail = ' '
    else:
        pass_fail = 'X'
        #print (range_list[index+1], max_list[index+1])
    print(str(count) + '\t', range_val, '\t|', min_val, max_val, '\t', mean, '\t|\t', first, last, pass_fail, ls[0])

    count += 1
print("#        Range  | Min   Max      Mean   |        First Last    Name")
#######################################

########|Validation Check|##########<
print("#####|Validation Check|####")
#store index number of invalid data
exclude_list = []
pass_list = []
if RangeReq > 0 or MaxReq > 0:
    for index in range(len(range_list)):
        ##print(index, range_list[index], max_list[index])
        #skip index = 0 (string headers)
        if index > 0:
            #Data check passes if either condition passes
            #(change 'or' to 'and' for more stringent check)
            if range_list[index] > RangeReq or max_list[index] > MaxReq:
                ##print(index, "Pass")
                pass_list.append(index)
            else:
                exclude_list.append(index)

failed_checks = len(exclude_list)
print("Failed Checks:", failed_checks)

#Remove invalid data from 'updated list'
if Remove_invalid_data == True:
    #iterating and deleting in forward direction will break the loop after 1st del operation
    for index, ls in reversed(list(enumerate(updated_lists))):
        if index in exclude_list:
            #print(index, "Excluded")
            del updated_lists[index]

if Remove_invalid_data == True:
    print('Data Excluded:', failed_checks, 'wells')
else:
    print('Data Excluded:', 'None')

if full_print == True and Remove_invalid_data == True:
    print( exclude_list[0:int(len(exclude_list)/2)])
    print( exclude_list[int(len(exclude_list)/2):])
###|Create updated CSV file|###
dataIO.multiCol_CSV('updated_plate_reader.csv', updated_lists)
###|Create grouping.R file|###
if generate_r_grping_file == True:
    pass
####################################>

#######################################################

#####Update Spreadsheet#####
#check if there is a "well_grouping" worksheet at index 1
wks1 = g_sheet.get_worksheet(1)
if type(wks1) is gspread.models.Worksheet:
    print("Worksheet @index 1:", wks1.title)
    if wks1.title != 'well_grouping': #check title of worksheet
        print("****Error: 'well_grouping' worksheet not setup, (or improperly named)")
        grouping = False
    else:
        print("*Grouping worksheet found*")
        grouping = True
#Check if there is a worksheet at index 2
wks2 = g_sheet.get_worksheet(2)
if type(wks2) is gspread.models.Worksheet:
    print("Worksheet @index 2:", wks2.title)
    if wks2.title == 'well_data' and full_sheet_update == True:    #check the title of the worksheet
        print("Delete", g_sheet.sheet1)
        g_sheet.del_worksheet(wks2)
    if wks2.title == 'well_labels':
        print("****Error: Move 'well_labels' worksheet to index 0 ")
        full_sheet_update = False
#if 2nd worksheet(@index=1) doesn't exist, create it
number_of_cols = len(updated_lists)
if g_sheet.get_worksheet(2) == None:
    g_sheet.add_worksheet('well_data', number_of_rows_csv, 201)

#setup well_data worksheet & well_grouping worksheet objects
well_data = g_sheet.worksheet('well_data')
well_grouping = g_sheet.worksheet('well_grouping')

####|Grouping Begin|##<
if generate_r_grping_file == True:
    g_list = get_grouping_data()
    group_names = dataIO.group_names(g_list)
    print('Group names:', group_names)
    dataIO.write_r_grping_file(g_list)
    #print(dataIO.group_items(g_list))
    dataIO.write_ggploter('grouping.R', g_list)
    print('***|grouping.R UPDATED|***')

########|R subprocess|########<
#TODO: handle case where generate_r_grping_file = False but Rub = True
if Rsub == True:
    print('****|Rscript plot_data.R EXECUTING|****')
    dataIO.exec_script2('Rscript', 'plot_data.R', group_names)
##############################>
####|Grouping End|##>

##########TO DO: Handle error that occurs when well_data sheet has less than 201 columns
if full_sheet_update == True:
    gsheet_update(updated_lists, number_of_cols)
    print(well_data.updated)
else:
    print("*Set \'post2google = True\' to upload data to the Google Spreadsheet*")
#######| END |########
#TODO Set run = False
end_time = RunTime.currentTime()#start-time
run_time = RunTime.calc_runTime(start_time, end_time)
print("############|END|##########")
print(run_time)
