import tkinter as tk
import random
from PIL import Image, ImageTk

pontuacao = 0

def iniciar_jogo():
    global pontuacao
    pontuacao = 0
    atualizar_pontuacao()
    aparecer_abobora()

def aparecer_abobora():
    largura_tela = root.winfo_width()
    altura_tela = root.winfo_height()

    margem_topo = 200
    margem_laterais = 20
    margem_inferior = 80

    x = random.randint(margem_laterais, largura_tela - margem_laterais - 80)
    y = random.randint(margem_topo, altura_tela - margem_inferior - 80)

    lbl_abobora.place(x=x, y=y)

def clicar_abobora(event):
    global pontuacao
    pontuacao += 1
    atualizar_pontuacao()
    aparecer_abobora()

def atualizar_pontuacao():
    lbl_pontuacao.config(text=f"PONTOS: {pontuacao}")


root = tk.Tk()
root.title("Jogo do Clique Fantasmagórico")
root.geometry("800x800")
root.configure(bg="black")


fonte_halloween = ("Comic Sans MS", 18)


lbl_instrucoes = tk.Label(root, text="CLIQUE NO FANTASMA PARA GANHAR PONTOS!", fg="orange", bg="black", font=fonte_halloween)
lbl_instrucoes.pack()

lbl_pontuacao = tk.Label(root, text="PONTOS: 0", fg="orange", bg="black", font=fonte_halloween)
lbl_pontuacao.pack()


btn_iniciar = tk.Button(root, text=">|| INICIAR JOGO", command=iniciar_jogo, fg="orange", bg="gray", font=fonte_halloween, width=15, height=2)
btn_iniciar.pack(pady=10)


imagem_abobora_original = Image.open("abobora.png.png").convert("RGBA")
imagem_abobora_resized = imagem_abobora_original.resize((80, 80), Image.LANCZOS)
imagem_abobora = ImageTk.PhotoImage(imagem_abobora_resized)

lbl_abobora = tk.Label(root, image=imagem_abobora, bg="black")
lbl_abobora.bind("<Button-1>", clicar_abobora)


root.mainloop()