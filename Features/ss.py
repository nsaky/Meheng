import keyboard

def take_screenshot():
    try:
        keyboard.press_and_release('win+print_screen')
        return "Taken a screenshot, of the whole screen."
    except:
        return "Unable to take a screenshot at the moment."