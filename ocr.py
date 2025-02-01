import cv2
import pytesseract
from tkinter import *
from tkinter.filedialog import askopenfilename

pytesseract.pytesseract.tesseract_cmd= r"c:\Program Files\Tesseract-OCR\tesseract.exe"

Tk().withdraw()

file_path = askopenfilename(
    title='Selecione uma imagem', 
    filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp")])

if not file_path:
    print("Nenhuma imagem foi selecionada. Encerrando o programa.")
else:
    img = cv2.imread(file_path)
              #############//#############
if img is None:
    print('Erro: Não foui possível carregar a imagem.Verifique o arquivo')
else:
    texto = pytesseract.image_to_string(img)
    pdf = pytesseract.image_to_pdf_or_hocr(img, extension="pdf")
    print('Texto detectado')
    print(texto)
    with open("texto.txt", "w", encoding="utf-8") as f:
            f.write(texto)

cv2.imshow("Imagem Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

corFont = '#3a6332'
corFundo = '#aaf99b'
fontGrande = 'Time 20'
fontNormal = 'Time 10'

#Tela

root = Tk()
root.title('Ascii')
root.resizable(width=True ,height=True)
root.geometry('700x900')
########################################################//###########################################################
#Lables

lable_titulo = Label(root, text='Editor de ocr', bg=corFundo, fg=corFont, font='Time 20 bold')
lable_titulo.place(width=700, height=50, x=0, y=0)
########################################################//###########################################################
#Buttons


root.mainloop()
