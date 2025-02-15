import tkinter as tk
from tkinter import filedialog, Scrollbar, Menu
from tkinter import Canvas as canvas
from PIL import Image, ImageTk
import importlib
import os

# Definição de cores
branco = "#ffffff" # Branco
azul = "#8f88ba" # Azul

# Variáveis globais
imagem_original = None # Imagem original carregada
imagem_editada = None
plugins = {} # Dicionário de plugins
zoom_factor = 1.0
canvas_pos_x, canvas_pos_y = 0, 0
mouse_x, mouse_y = 0, 0 


def atualizar_lista_plugins():
    for widget in frame_plugins.winfo_children():
        widget.destroy()
    for nome_plugin, (modulo, icone) in plugins.items():
        btn_efeito = tk.Button(
            frame_plugins,
            text=f"{icone} {nome_plugin}",
            command=lambda m=modulo: aplicar_efeito(m),
            width=18,
            anchor="w",
        )
        btn_efeito.pack(pady=2)
    btn_refresh = tk.Button(
        frame_plugins,
        text="🔄 Refresh Plugins",
        anchor="w",
        command=atualizar_plugins,
        width=18,
    )
    btn_refresh.pack(pady=5)



def aplicar_efeito(modulo):
    global imagem_editada
    if imagem_original:
        imagem_editada = modulo.aplicar(imagem_original.copy())
        exibir_imagem(imagem_editada)

def atualizar_plugins():
    # carregar_plugins()
    atualizar_lista_plugins()



def abrir_imagem():
    global imagem_original, imagem_editada, zoom_factor
    caminho = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if caminho:
        imagem_original = Image.open(caminho)
        imagem_editada = imagem_original.copy()
        zoom_factor = 1.0 
        exibir_imagem(imagem_editada)

def salvar_imagem():
    if imagem_editada:
        caminho = filedialog.asksaveasfilename(
            defaultextension=".png",
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
    canvas.img_tk = img_tk
    canvas.delete("all")
    canvas.create_image(
        canvas.winfo_width() // 2,
        canvas.winfo_height() // 2,
        anchor=tk.CENTER,
        image=img_tk,
    )
    canvas.config(scrollregion=canvas.bbox("all"))


def restaurar_original():
    global imagem_editada
    if imagem_original:
        imagem_editada = imagem_original.copy()
        exibir_imagem(imagem_editada)



def zoom(event):
    global zoom_factor
    if event.delta > 0:
        zoom_factor = 1.1
    elif event.delta < 0:
        zoom_factor = 0.9
    exibir_imagem(imagem_editada)



def iniciar_movimento(event):
    global mouse_x, mouse_y, canvas_pos_x, canvas_pos_y
    mouse_x, mouse_y = event.x, event.y
    canvas_pos_x, canvas_pos_y = canvas.xview(), canvas.yview()



def mover_imagem(event):
    global mouse_x, mouse_y
    dx = (mouse_x - event.x) / 50
    dy = (mouse_y - event.y) / 50
    canvas.xview_moveto(canvas_pos_x[0] + dx)
    canvas.yview_moveto(canvas_pos_y[0] + dy)

# 📌 Criar interface gráfica
root = tk.Tk()
root.title("Pythonshop")
root.geometry("1024x800")
                         ##########//##########
menu_superior = tk.Menu(root)
root.config(menu=menu_superior)
menu_arquivo = tk.Menu(menu_superior, tearoff=0)
menu_arquivo.add_command(label="📂 Abrir", command=abrir_imagem)
menu_arquivo.add_command(label="💾 Salvar", command=salvar_imagem)
menu_arquivo.add_command(label="🔄 Restaurar", command=restaurar_original)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="❌ Sair", command=root.quit)
menu_superior.add_cascade(label="Arquivo", menu=menu_arquivo)

frame_principal = tk.Frame(root)
frame_principal.pack(fill=tk.BOTH, expand=True)

frame_menu = tk.Frame(frame_principal, width=200, bg=azul)
frame_menu.pack(side=tk.LEFT, fill=tk.Y)

lbl_filtros = tk.Label(frame_menu, text="Opções", bg=azul, font=("Arial", 12, "bold"))
lbl_filtros.pack(pady=10)

btn_abrir = tk.Button(
    frame_menu, text=" Abrir Imagem", anchor="w", command=abrir_imagem, width=18
)
btn_abrir.pack(pady=5)

btn_salvar = tk.Button(
    frame_menu, text='Salvar', ancor='w', command=restaurar_original, width=18
)
btn_salvar.pack(pady=5)

btn_restaurar = tk.Button(
    frame_menu, text="Restaurar", anchor="w", command=restaurar_original, width=18
)
btn_restaurar.pack(pady=5)

lbl_filtros = tk.Label(frame_menu, text="Filtros", bg=azul, font=("Arial", 12, "bold"))
lbl_filtros.pack(pady=10)

frame_canvas = tk.Frame(frame_principal)
frame_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

canvas = canvas(frame_canvas, bg="#000000")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



root.mainloop()
