import dataIO
import dataCowboy

my_list = ["well_1", "well_2", "well_3"]

full_lists = [ ["well_1", 0.25, 0.50, 0.75], ["well_2", 0.10, 0.20, 0.30], ["well_3", 0.33, 0.66, 0.99] ]

#print(my_list)
#print(full_lists)


#print(dataIO.colList_to_rowList(full_lists))
print(dataIO.list_n(3))
print(dataIO.cols_to_rows_list(full_lists))

dataIO.multiCol_CSV("by_row_test.csv",full_lists)