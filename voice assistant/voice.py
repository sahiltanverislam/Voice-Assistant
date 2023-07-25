import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
   recognizer=sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening...")
       recognizer.adjust_for_ambient_noise(source)     
       audio = recognizer.listen(source)
       try:
           print("recognizin...")
           data = recognizer.recognize_google(audio)
           print(data)
       except sr.UnknownValueError:
           print("Not Understand")

def speechtext(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
speechtext("hello and welcome to techno india gruop")
speechtext("never ever give up")
speechtext("Congratulations!!!!you are a employee of this company")
speechtext("Best wishes for you")
speechtext("thanks")