import cv2
import mediapipe as mp
import subprocess
import webbrowser
import time

mp_mao = mp.solutions.hands.Hands(max_num_hands=2)
desenho = mp.solutions.drawing_utils
ultimo_gesto = ""
tempo_ultimo = 0

def contar_dedos(pontos):
    dedos = 0

    if pontos[8].y < pontos[6].y: dedos += 1
    if pontos[12].y < pontos[10].y: dedos += 1
    if pontos[16].y < pontos[14].y: dedos += 1
    if pontos[20].y < pontos[18].y: dedos += 1
    
    if abs(pontos[4].x - pontos[2].x) > 0.1:
        dedos += 1

    return dedos


cam = cv2.VideoCapture(0)

while True:
    ok, frame = cam.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = mp_mao.process(rgb)

    if resultado.multi_hand_landmarks:
        for mao in resultado.multi_hand_landmarks:
            desenho.draw_landmarks(frame, mao, mp.solutions.hands.HAND_CONNECTIONS)
            dedos = contar_dedos(mao.landmark)
            agora = time.time()
            print(f"Dedos: {dedos}")



            if dedos == 2:
                subprocess.run(["start", "msedge"], shell=True)
                print("📝 Mão aberta → Abrir Edge")
                ultimo_gesto = "aberta"
                tempo_ultimo = agora

            elif dedos == 0 and (ultimo_gesto != "fechada" or agora - tempo_ultimo > 3):
                webbrowser.open("https://www.google.com")
                print("🌐 Mão fechada → Abrir Google")
                ultimo_gesto = "fechada"
                tempo_ultimo = agora

            elif dedos == 1:
                webbrowser.open("https://www.youtube.com/watch?v=BFPf7wrLWxg&ab_channel=AnthonyMendoza")
                print("🌐 Mão aberta → Abrir Google")
                ultimo_gesto = "aberta"
                tempo_ultimo = agora



    cv2.imshow("Detecção de Gestos", frame)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
