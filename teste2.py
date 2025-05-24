import cv2                     # Biblioteca para capturar vídeo e manipular imagens
import mediapipe as mp         # Biblioteca para detectar pontos do rosto
import time                    # Biblioteca para contar o tempo
import winsound                # Biblioteca para tocar som no Windows

TEMPO_LIMITE = 2  

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5)

tempo_ausente = 0            
olhos_detectados = True      

cam = cv2.VideoCapture(0)

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
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)  # círculo verde maior para os olhos

            # Desenha o ponto do nariz (landmark 1)
            nariz = face_landmarks.landmark[1]
            nariz_x, nariz_y = int(nariz.x * w), int(nariz.y * h)
            cv2.circle(frame, (nariz_x, nariz_y), 6, (0, 0, 255), -1)  # círculo vermelho para o nariz

        olhos_detectados = True
        tempo_ausente = time.time()
    else:
        if olhos_detectados:
            olhos_detectados = False
            tempo_ausente = time.time()
        else:
            if time.time() - tempo_ausente > TEMPO_LIMITE:
                print("⚠️ Atenção! Olhos não detectados por mais de 2 segundos!")
                winsound.Beep(1000, 500)
                tempo_ausente = time.time()

    cv2.imshow("Detecção de Olhos e Nariz", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()