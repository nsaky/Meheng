import pyttsx3

#Windows Based
def Speak(Text):
    engine= pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate', 170)
    print("")
    print(f"Meheng: {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

