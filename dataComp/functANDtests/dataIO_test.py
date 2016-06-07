import dataIO
import random

col1 = []
col2 = []
header_list = ['Alpha', 'Bravo']


for i in range(50):
    col1.append(1+i)
    col2.append(random.randrange(1,25))

print(header_list[0],len(col1), col1)
print(header_list[1],len(col2), col2)

col_list = [col1, col2]
unequal_list = [col1, header_list]

print(col_list)

dataIO.singleCol_CSV('test1.csv', header_list[0], col1)
dataIO.doubleCol_CSV('test2.csv', header_list, col_list)
#dataIO.doubleCol_CSV('errorTest.csv', header_list, unequal_list)
