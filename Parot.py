import speech_recognition as sr
import pyttsx3

rec = sr.Recognizer

engine = pyttsx3.init()
voices = engine.getProperty('voices')


for voice in voices:
    print(voice)

def speak(text):
    global engine
    engine.say(text)
    engine.runAndWait()
