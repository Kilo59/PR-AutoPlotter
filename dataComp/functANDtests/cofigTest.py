from configparser import SafeConfigParser
import dataIO
import RunTime
start_time = RunTime.currentTime()#start-time

RunTime.pause(1)

parser = SafeConfigParser()
parser.read('config.txt')

print( parser.getfloat('tolerance', 'rangeReq') )
print( parser.getfloat('tolerance', 'maxReq') )
#print( dataIO.get_tolerance('rangeReq') )
#print( dataIO.get_tolerance('maxReq') )

run_bol = parser.getboolean('start_conditions', 'run')
#run_bol = dataIO.get_start_cond('run')
if run_bol == True:
    print(run_bol)
else:
    print('Quit')

gen_grouping_file = dataIO.get_R_options("gen_grping_file")
if gen_grouping_file == True:
    print("Generate R file")
else:
    print("Skip R file")

grping_file = 'grouping.R'
system_time = RunTime.system_time()
f = open(grping_file, 'w')
f.write("#file: "+grping_file+"\n#Time: "+RunTime.system_time())
f.close()

end_time = RunTime.currentTime()#start-time
run_time = RunTime.calc_runTime(start_time, end_time)
print("############|END|##########")
print(run_time)