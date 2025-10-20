from tkinter import *
import pyautogui
from time import sleep

root = Tk()

root.title("Buscador Goooogle")

root.geometry("400x800")
root.resizable(width=False, height=False)

label = Label(root, text="MEU BUSCADOR", font=("Arial", 22))
label.pack(pady=10)

#img = PhotoImage(file="Buscador_Goooogle.png")
#Label(root, image=img).pack()

label = Label(root, text="Digite o que deseja buscar", font=("Arial", 20))
label.pack(pady=10)

entry = Entry(root, font=("Arial", 20))
entry.pack(pady=0, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="EXPLORE", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="BRAWLERS", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="EVENTS", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="GAMEPLAY", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="COMUNITY", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)


def buscar_na_wiki_do_bs():
    pyautogui.hotkey("win", "r")
    pyautogui.write("www.google.com")
    pyautogui.press("enter")
    sleep(2)
    
    pyautogui.whrite('brawl stars wiki :)')
    sleep(2)
    pyautogui.press("enter")

    pyautogui.moveTo(x=510, y=552)
    pyautogui.doubleClick()


    button = Button(root, text="EXPLORE", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="BRAWLERS", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="EVENTS", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="GAMEPLAY", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="COMUNITY", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

#BOTAO        EXPLORE   pyautogui.moveTo(x=675, y=879)
#BOTAO        BRAWLERIS pyautogui.moveTo(x=1264, y=889)
#BOTAO        EVENTIS   pyautogui.moveTo(x=1182, y=891)   
#BOTAO        GAMIPLAI  pyautogui.moveTo(x=983, y=875) 
#BOTAO        COMUNITY  pyautogui.moveTo(x=675, y=879) 

    
    pyautogui.write(entry.get())
    pyautogui.press("enter")



button.config(command=buscar_na_wiki_do_bs)

root.mainloop()
