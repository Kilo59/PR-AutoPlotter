#Author:SpaceTuna8
import dataIO
import subprocess
import os

current_directory = os.getcwd()
print(current_directory)

'''
# => [1, 2, 3, ... 49, 50]
data_list = [x for x in range(1,51)]
args = ''.join(str(i) for i in data_list)
str(data_list)
dataIO.singleCol_CSV("Py_R_test1.csv", "ColumnHeader", data_list)
'''

# Variable number of args in a list
args = ['11', '3', '9', '42']

#define command and argument
command = 'Rscript'
script = 'fromPython.R'
path2script = current_directory + '\\' + script
print(path2script)

#build subprocess command
cmd = [command, path2script] + args
print(cmd)

#check_output will run command and store to result
x = subprocess.check_output(cmd, universal_newlines=True) #shell=True unecessary?

print('The maximum of the numbers is:', x)

'''
To quote from the documentation: The only time you need to specify shell=True on Windows is 
when the command you wish to execute is built into the shell (e.g. dir or copy). 
You do not need shell=True to run a batch file or console-based executable.
'''
