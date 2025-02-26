from threading import Thread

#Listen and speak function
from Body.Listen import MicExecution
from Body.Speak import Speak

#Importing Brain Function
from Brain.Brain import meheng_brain

#Importing Backend functions
from Backend.conversation_logging import conversation_logs
from Backend.admin_conversation_logging import admin_conversation_logs

#Importing Features
from Features.battery import battery_info
from Features.click_photo import click_photo
from Features.internet import get_speed
from Features.jokes import jokes
from Features.news import GetNews
from Features.Open import OpenExe
from Features.songs import play_song
from Features.ss import take_screenshot
from Features.tell_date import get_local_date
from Features.tell_time import get_local_time
from Features.userlocation import get_user_location
from Features.yt import search_yt
from Features.yt import play_yt_video

def TaskExecution(Query):
    try:
        Task=str(Query).lower()

        if "battery" in Task or "battery percentage" in Task or "battery health" in Task:
            Value=battery_info()
            return Value
        elif "take a photo" in Task or "take a picture" in Task or "click" in Task or "picture" in Task:
            Value=click_photo()
            return Value
        elif "internet" in Task and ("speed" in Task or "test" in Task):
            Value = get_speed()
            return Value
        elif "joke" in Task or "make me laugh" in Task:
            Value = jokes()
            return Value
        elif "news" in Task or "headlines" in Task:
            Value = GetNews()
            return Value
        elif "open" in Task or "visit" in Task or "launch" in Task or "start" in Task:
            Value = OpenExe(Query)
            return Value
        elif "play" in Task and ("song" in Task or "music" in Task):
            Value = play_song()
            return Value
        elif "screenshot" in Task or "capture screen" in Task:
            Value = take_screenshot()
            return Value
        elif "date" in Task or "today's date" in Task:
            Value = get_local_date()
            return Value
        elif "time" in Task or "current time" in Task:
            Value = get_local_time()
            return Value
        elif "location" in Task or "where am i" in Task:
            Value = get_user_location()
            return Value
        elif "search" in Task and "youtube" in Task:
            keyword=Task.replace("search on youtube ","")
            Value = search_yt(keyword)
            return Value
        elif "play" in Task and "youtube" in Task:
            keyword=Task.replace("play on youtube ","").replace(" ","_")
            Value = play_yt_video(keyword)
            return Value
        else:
            Value=meheng_brain(Task)
            return Value
    except Exception as e:
        return "Sorry, Unable to respond to that question at the moment."

def talk_to_meheng(user_id, firstname, status_label):
    def execute_task():
        while True:
            # Display "Listening" status
            status_label.configure(text="Listening")
            status_label.update()

            Data = MicExecution()
            Data = str(Data)

            if Data == "None":
                status_label.configure(text="Ready")
                status_label.update()
                break

            # Display "Responding" status
            status_label.configure(text="Responding")
            status_label.update()

            if "hi" in Data or "hi meheng" in Data:
                response = f"Hi {firstname}"
                Speak(response)
                conversation_logs(user_id, Data, response)
            elif "who am i" in Data or "what is my name" in Data:
                response = f"You are {firstname}."
                Speak(response)
                conversation_logs(user_id, Data, response)
            elif "who made you" in Data or "who programmed you" in Data:
                response = "I was programmed by Yasir"
                Speak(response)
                conversation_logs(user_id, Data, response)
            elif "what is your name" in Data or "who are you" in Data:
                response = "I am Meheng. Your Personal A. I. Voice Assistant"
                Speak(response)
                conversation_logs(user_id, Data, response)
            else:
                response = TaskExecution(Data)
                Speak(response)
                conversation_logs(user_id, Data, response)

            # Reset status after responding
            status_label.configure(text="Ready")
            status_label.update()

    # Start the task in a separate thread
    thread = Thread(target=execute_task)
    thread.start()

def admin_talk_to_meheng(admin_id, firstname, status_label):
    def execute_task():
        while True:
            # Display "Listening" status
            status_label.configure(text="Listening")
            status_label.update()

            Data = MicExecution()
            Data = str(Data)

            if Data == "None":
                status_label.configure(text="Ready")
                status_label.update()
                break

            # Display "Responding" status
            status_label.configure(text="Responding")
            status_label.update()

            if "hi" in Data or "hi meheng" in Data:
                response = f"Hi {firstname}"
                Speak(response)
                admin_conversation_logs(admin_id, Data, response)
            elif "who am i" in Data or "what is my name" in Data:
                response = f"You are {firstname}."
                Speak(response)
                admin_conversation_logs(admin_id, Data, response)
            elif "who made you" in Data or "who programmed you" in Data:
                response = "I was programmed by Yasir"
                Speak(response)
                admin_conversation_logs(admin_id, Data, response)
            elif "what is your name" in Data or "who are you" in Data:
                response = "I am Meheng. Your Personal A. I. Voice Assistant"
                Speak(response)
                admin_conversation_logs(admin_id, Data, response)
            else:
                response = TaskExecution(Data)
                Speak(response)
                admin_conversation_logs(admin_id, Data, response)

            # Reset status after responding
            status_label.configure(text="Ready")
            status_label.update()

    # Start the task in a separate thread
    thread = Thread(target=execute_task)
    thread.start()