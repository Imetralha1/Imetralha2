import tkinter as tk

root = tk.Tk()
root.title("BS quiz")
root.geometry("1024x800")


# 📌 Criar layout principal


botao = tk.Button(text="Abrir nova janela", Arial=12)
botao.pack(expand=True, fill='both', padx=50, pady=50)

root1 = tk.Tk()
root1.title("BS quiz")
root1.geometry("1024x800")