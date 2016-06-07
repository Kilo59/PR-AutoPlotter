#Author:SpaceTuna8
import dataIO

# => [1, 2, 3, ... 49, 50]
data_list = [x for x in range(1,51)]

dataIO.singleCol_CSV("Py_R_test1.csv", "ColumnHeader", data_list)
