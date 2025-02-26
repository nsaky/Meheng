import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    try:
        Query=str(Query).lower()
        
        if "visit" in Query:
            Nameofweb=Query.replace("visit ", "")
            Link=f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)
            return f"Visited {Nameofweb}"
        
        elif "launch" in Query:
            Nameofweb=Query.replace("launch ", "")
            Link=f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)
            return f"Launched {Nameofweb}"

        elif "open" in Query:
            Nameoftheapp=Query.replace("open ","")
            pyautogui.press('win')
            sleep(1)
            keyboard.write(Nameoftheapp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
            return f"Opened {Nameoftheapp}"
        
        elif "start" in Query:
            Nameoftheapp=Query.replace("start ","")
            pyautogui.press('win')
            sleep(1)
            keyboard.write(Nameoftheapp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
            return f"Started {Nameoftheapp}"
    except:
        return "Unable to open the requested application or website."