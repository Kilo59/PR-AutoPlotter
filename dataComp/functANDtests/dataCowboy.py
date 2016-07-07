#DataCowboy.py
#SpaceTuna8

#Accepts a list of lists and places every item into their own list.
#Intended to correspond to the 2 10x10 wells used by the Biocscreen plate reader
#Although not a requirement for this function the list_of_columns is expected to contain 20 lists with 10 items each)
#Well numbers should correspond to the plate layout.
#Top left well = well_1 | bottom left = well_10 | top right = well 91 OR 191 | bottom right = well 100 OR 200
def pl_rdr_labels(list_of_columns):
    colA = []
    colB = []
    colC = []
    colD = []
    colE = []
    colF = []
    colG = []
    colH = []
    colI = []
    colJ = []
    colK = []
    colL = []
    colM = []
    colN = []
    colO = []
    colP = []
    colQ = []
    colR = []
    colS = []
    colT = []
    column_list = [colA, colB, colC, colD, colE, colF, colG, colH, colI, colJ, colK, colL, colM, colN, colO, colP, colQ, colR, colS, colT]
    for row in list_of_columns:
        for cell, index in zip(row, range(len(column_list))):
            column_list[index].append(cell)
    return column_list

#Merge a list of lists into a single list
#uses pl_rdr_labels
def pl_rdr_single_list(list_of_columns):
    single_list = []
    list_of_list = pl_rdr_labels(list_of_columns)
    for a_list in list_of_list:
        for item in a_list:
            single_list.append(item)
    return single_list

#replace Column Headers
#iterate through the list of lists and replace the first item in each list with an item from the replacement_list
def header_replacement(list_of_lists, replacement_list):
    for list_index, ls in enumerate(list_of_lists):
        #skip 'Time' list
        if list_index > 0 and list_index <= len(replacement_list):
            ls[0] = replacement_list[list_index-1]
    return list_of_lists

'''
####Accept a single list (from CSV) stored row by row
##Example [A1, B1, C1, A2, B2, C2, A3, B3, C3
def single_list_to_grouped_list(single_list):
    list_of_list = []
    for i in single_list:

    return list_of_list
'''
