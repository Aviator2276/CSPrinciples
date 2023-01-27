import time

setTime = input("What do you want to set the timer to? (minutes:seconds - ##:##) ")
if not setTime[0].isdecimal() or not setTime[1].isdecimal() or not setTime[3].isdecimal() or not setTime[4].isdecimal() or int(setTime[3]) > 5 and int(setTime[4]) >= 0:
    print("Error: Wrong syntax!")
    quit()
minutes = setTime[0] + setTime[1]
minutes = int(minutes)
seconds = setTime[3] + setTime[4]
seconds = int(seconds)

timer = (minutes * 60) + seconds
while timer != 0:
    addZeroSec = ''
    addZeroMin = ''
    timerMin = int(timer / 60)
    timerSec = int(timer % 60)
    if timerSec < 10:
        addZeroSec = 0
    elif timerSec == 0:
        addZeroSec = 0
    if timerMin < 10:
        addZeroMin = 0
    elif timerMin == 0:
        addZeroMin = 0
    print(str(addZeroMin) + str(timerMin) + ":" + str(addZeroSec) + str(timerSec))
    time.sleep(1)
    timer -= 1
print("Done")