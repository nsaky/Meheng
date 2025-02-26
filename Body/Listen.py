import speech_recognition as sr
from googletrans import Translator

#1- listen function
def Listen():
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en")
    except:
        return ""
    
    query=str(query).lower()
    return query

#2- Translation
def TranslationHinToEng(Text):
    line=str(Text)
    translate=Translator()
    try:
        result= translate.translate(line)
        data=result.text
        print(f"You: {data}.")
        return data
    except:
        print("Translation Error")

#3- Connect
def MicExecution():
    query=Listen()
    if len(query)>2:
        data=TranslationHinToEng(query).lower()
        return data

