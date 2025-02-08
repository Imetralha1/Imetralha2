import tkinter as tk
from tkinter import filedialog, Canvas, Scrollbar, Menu
from PIL import Image, ImageTk
import importlib
import os

corFont = '#3a6332'
corFundo = '#aaf99b'
fontGrande = 'Time 20'
fontNormal = 'Time 10'

imagem_original = None
imagem_editada = None
plugins = {}
zoom_factor = 1.0
canvas_pos_x, canvas_pos_y = 0, 0
mouse_x, mouse_y = 0, 0

def abrir_imagem():
    global imagem_original, imagem_editada, zoom_factor
    caminho = filedialog.askopenfilename(filetypes=[
        ("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if caminho:
        imagem_original = Image.open(caminho)
        imagem_editada = imagem_original.copy()
        zoom_factor = 1.0
        # exibir_imagem(imagem_editada)

def salvar_imagem():
    if imagem_editada:
        caminho = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")],
        )

        if caminho:
            imagem_editada.save(caminho)

def exibir_imagem(img):
    largura, altura = img.size
    nova_largura = int(largura * zoom_factor)
    nova_altura = int(altura * zoom_factor)
    img_resized = img.resize((nova_largura, nova_altura), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_resized)
    Canvas.img_tk = img_tk
    Canvas.delete = ('all')
    Canvas.create_image(
        Canvas.winfo_width() // 2,
        Canvas.winfo_height() // 2,
        anchor=tk.CENTER,
        image=img_tk,
    )
########################################################//###########################################################
#Tela
root = tk.Tk()
root.title('PhytonShop')
root.resizable(width=True ,height=True)
root.geometry('1024x700')
########################################################//###########################################################
#Menu
menu_superior = tk.Menu(root)
root.config(menu=menu_superior)
menu_arquivo = tk.Menu(menu_superior, tearoff=0)
menu
########################################################//###########################################################
#Buttons


root.mainloop()
