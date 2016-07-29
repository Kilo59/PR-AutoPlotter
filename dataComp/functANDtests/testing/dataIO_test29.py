from dataIO import write_line_a
from dataIO import append_list_of_string
string1 = '1st time'
string2 = '2nd time'
string3 = '3rd time'
filename = 'line_test.txt'
string_list = [string1, string2, string3]
#write_line_a(filename, string1)
#write_line_a(filename, string2)
print(string_list)
append_list_of_string(filename, string_list)
