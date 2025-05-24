import cv2
import mediapipe as mp
import time
import tkinter as tk
from threading import Thread

TEMPO_LIMITE = 2  

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5)

tempo_ausente = 0            
olhos_detectados = True      

cam = cv2.VideoCapture(0)

def abrir_alerta():
    # Função que cria uma janela Tkinter com a mensagem de alerta
    root = tk.Tk()
    root.title("Alerta de Atenção")
    root.geometry("300x150")
    label = tk.Label(root, text="⚠️ Atenção! Olhos não detectados!", font=("Arial", 14))
    label.pack(expand=True)
    botao = tk.Button(root, text="Fechar", command=root.destroy)
    botao.pack(pady=10)
    root.mainloop()

alerta_aberto = False

while True:
    ok, frame = cam.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultado = face_mesh.process(rgb)

    if resultado.multi_face_landmarks:
        for face_landmarks in resultado.multi_face_landmarks:
            h, w, _ = frame.shape

            # Desenha os pontos dos olhos
            for i in [33, 133, 362, 263]: 
                ponto = face_landmarks.landmark[i]
                x, y = int(ponto.x * w), int(ponto.y * h)   
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            # Desenha o ponto do nariz
            nariz = face_landmarks.landmark[1]
            nariz_x, nariz_y = int(nariz.x * w), int(nariz.y * h)
            cv2.circle(frame, (nariz_x, nariz_y), 6, (0, 0, 255), -1)

        olhos_detectados = True
        tempo_ausente = time.time()
        alerta_aberto = False  # Resetar estado do alerta
    else:
        if olhos_detectados:
            olhos_detectados = False
            tempo_ausente = time.time()
        else:
            if time.time() - tempo_ausente > TEMPO_LIMITE and not alerta_aberto:
                alerta_aberto = True
                # Abrir a janela de alerta numa thread para não travar o loop
                Thread(target=abrir_alerta, daemon=True).start()

    cv2.imshow("Detecção de Olhos e Nariz", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

