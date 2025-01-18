from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pywhatkit

corFont = '#3a6332'
corFundo = '#aaf99b'
fontGrande = 'Time 20'
fontNormal = 'Time 10'

def abrir():
    global filedialog

    filename = filedialog.askopenfilename(title='Escolha uma imagem para converter para ASCII...', initialdir=os.getcwd(), filetypes=(('PNG file','*.png'),('JPG file','*.jpg')))
root = Tk()
root.title('Ascii')
root.resizable(width=True ,height=True)
root.geometry('700x900')

lable_titulo = Label(root, text='Aqui o meu titulo', bg=corFundo, fg=corFont, font='Time 20 bold')
lable_titulo.place(width=700, height=50, x=0, y=0)


btnAbrir = Button(root, text='Abrir', command=abrir, font=fontNormal, bg=corFundo, fg=corFont)
btnAbrir.place(width=700, height=100, x=0, y=0)


btnnome = Button(root, text='Gravar', command=abrir, font=fontNormal, bg=corFundo, fg=corFont)
btnnome.place(width=700, height=200, x=0, y=0)




root.mainloop()
