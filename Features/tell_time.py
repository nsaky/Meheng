from datetime import datetime

def get_local_time():
    try:
        current_time = datetime.now().strftime("%I. %M. %p")
        return f"It is {current_time} right now"
    except:
        return "Unable to get the time at the moment."
    