from tkinter import *
from pynput import mouse
from time import time
import os
from datetime import datetime
import pyautogui 

start_time = None
monitoring = False
listener = None

root = Tk()
root.resizable(False, False)
root.geometry('300x300+400+350')
root.title('Controle de Monitoramento')

button1 = Button(root, text='Start', font=('Arial', 18))
button1.pack()

button2 = Button(root, text='Stop', font=('Arial', 18))

if not os.path.exists('Oin'):
    os.makedirs('Oin')
if not os.path.exists('Oin'):
    os.makedirs('Oin')

def ts():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filepath = f"Oin/{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)

def on_click(x, y, button, pressed):
    global start_time

    if pressed:
        start_time = time()
    elif start_time and time() - start_time >= 2:
        print('Click por mais de 2 seg.')
        ts()
        start_time = None

def Start():
    global monitoring, listener

    button1.pack_forget()
    button2.pack()

    if not monitoring:
        print('Start')
        monitoring = True
        listener = mouse.Listener(on_click=on_click)
        listener.start()

def Stop():
    global monitoring, listener

    print('Stop')
    button2.pack_forget()
    button1.pack()

    if monitoring:
        monitoring = False
        if listener:
            listener.stop()
            listener = None

button1.config(command=Start)
button2.config(command=Stop)

root.mainloop()