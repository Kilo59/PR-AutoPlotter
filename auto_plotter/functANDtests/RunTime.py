#RunTime.py
import datetime #to calculate script run-time
import time

#Functions
def currentTime():
    date = time.localtime(time.time())
    now = datetime.datetime.now()
    hour = int('%d' % now.hour)
    minute = int('%d' % now.minute)
    second = int('%d' % now.second)
    Time = (hour*3600) + (minute*60) + second
    return Time

def system_time():
    date = time.localtime(time.time())
    now = datetime.datetime.now()
    hour = '%d' % now.hour
    minute = '%d' % now.minute
    second = '%d' % now.second
    currentTime = str(hour) +':'+ str(minute) +':'+ str(second)
    return currentTime

def calc_runTime(start, end):
    Time = end - start
    seconds = Time
    if Time >= 1:
        if Time > 60:
            minutes = int(Time / 60)
            seconds = Time % 60
            return 'RunTime: ' + str(minutes) + ' minute ' + str(seconds) + ' second'
        else:
            return 'RunTime: ' + str(Time) + ' second(s)'
    if Time < 1:
        return 'RunTime: <1 second'

def pause(seconds_to_pause):
    time.sleep(seconds_to_pause)
    return

#start_time = currentTime()#Store script start-time
#time.sleep(62)
#end_time = currentTime()#Store script end-time
#runTime = calc_runTime(start_time, end_time)
#print(runTime)
