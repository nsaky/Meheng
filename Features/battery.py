import psutil 

def convertTime(seconds): 
    try:
        minutes, seconds = divmod(seconds, 60) 
        hours, minutes = divmod(minutes, 60) 
        return (hours, minutes, seconds) 
    except:
        return "I am sorry, Unable to get battery information at the moment"

def battery_info():
    try:
        battery = psutil.sensors_battery() 
        percentage=battery.percent
        plugged_in=battery.power_plugged
        battery_left=convertTime(battery.secsleft)
        if plugged_in==False:
            return "You have "+str(percentage)+" percent battery left, "+" which will sustain for about "+str(battery_left[0])+" hours "+str(battery_left[1])+" minutes and "+str(battery_left[2])+" seconds. Your device is currently not plugged in" 
        else:
            return "You have "+str(percentage)+" percent battery left, "+" which will sustain for about "+str(battery_left[0])+" hours "+str(battery_left[1])+" minutes and "+str(battery_left[2])+" seconds, if the power source is plugged out. Your device is currently plugged in."
    except:
         return "I am sorry, Unable to get battery information at the moment"
