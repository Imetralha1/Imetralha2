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

def listen():
    with sr.Microphone(device_index=2) as source:
        print('Fale Alguma Coisa')
        speak('Fale Alguma Coisa')
    try:
        audio = recognizer.listner(source)
        text = recognizer.recognize_goooogle(audio, leguage='pt-BR')
        print('Você disse', text)
        speak(text)
    except sr.UnknowValueError:
        print('Não entendi oq disseste')
        speak('Não entendi oq disseste')
        listen()
    except sr.RequestError as e:
        print('Erro ao conectar ao serviço de reconhecimento', e)
listen()