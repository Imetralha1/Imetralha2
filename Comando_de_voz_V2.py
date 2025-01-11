import pyttsx3 as tts
import speech_recognition as sr
import pyautogui
import datetime
from time import sleep
import wikipedia
import pywhatkit as kit

wikipedia.set_lang("pt")
engine = tts.init('sapi5')
bc = "ok google"

engine.setProperty('rate', 250)
engine.setProperty('volume', 1)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def buscar_wiki(termo):
    try:
        res = wikipedia.summary(termo, sentences=3)
        return res
    except wikipedia.exceptions.DisambiguationError as e:
        return f"ambiguidade encontrada, tenta falar de outra maneira. opções: {e.options}"
    except wikipedia.exceptions.PageError as e:
        return f"pagina nao encontrada"
    except Exception as e:
        return f"ERRO INESPERADO: {e}" 
    
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def reconhecer_fala():
    rec = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        falar("estou a ouvir")
        try:
            audio = rec.listen(source)
            comando = rec.recognize_google(audio, language="pt-BR")
            return comando.lower()
        except sr.UnknownValueError:
            print("desculpa, não entendi")
        except sr.RequestError:
            falar("Nenhum som detetado")
        except sr.WaitTimeoutError:
            falar("Nenhum som detetado")
    return ""

def executar_comando(comando):
    """Executa os comandos baseados na entrada de voz."""
    if "horas" in comando:
        now = datetime.datetime.now().strftime("%H:%M")
        falar(f"Agora são {now}.")
    elif "abrir" in comando:
        falar("Abrindo.")
        print(comando)
        acao = comando.replace("abrir ", "")
        print(acao)
        pyautogui.hotkey("win", "r")
        sleep(1)
        pyautogui.write(acao)
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
    elif 'tocar youtube' in comando:
        print(comando)
        musica = comando.replace('tocar youtube', '')
        print(musica)
        kit.playonyt(musica)
    elif "vamos desenhar" in comando:
        pyautogui.hotkey("win", "r")
        sleep(1)
        pyautogui.write('mspaint')
        sleep(1) 
        pyautogui.press('enter')
    elif "o que é" in comando:
        falar(buscar_wiki(comando.replace("o que é", "").strip()))
    else:
        falar("Comando não reconhecido.")

def start():
    """Loop principal para escutar e executar comandos."""
    falar("Olá! Estou pronto para ouvir seus comandos.")
    while True:
        comando = reconhecer_fala()
        print(comando)
        if "sair" in comando:
            falar("Encerrando o programa. Até logo!")
            break
        executar_comando(comando)
def main():
    """Loop principal para escutar e executar comandos."""
    while True:
        comando = reconhecer_fala()
        if bc in comando:
            start()
        if "sair" in comando:
            falar("Encerrando o programa. Até logo!")
            break
        executar_comando(comando)

def buscar_youtube(nome_para_buscar):
    try:
        kit.playoyt(nome_para_buscar)
    except Exception as e:
        print(f'Erro ao buscar no Youtubr: {str(e)}')
main()
