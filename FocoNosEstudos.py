# ✅ Importar as bibliotecas necessárias
import cv2                     # Biblioteca para capturar vídeo e manipular imagens
import mediapipe as mp         # Biblioteca para detectar pontos do rosto
import time                    # Biblioteca para contar o tempo
import winsound                # Biblioteca para tocar som no Windows

# 🔴 Definimos um limite de tempo (em segundos) para acionar o alerta se os olhos não forem detectados
TEMPO_LIMITE = 2  

# ✅ Inicialização do detector de rosto do MediaPipe
mp_face_mesh = mp.solutions.face_mesh  # Carregando o modelo de detecção de rosto
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5)  # Definindo a confiança mínima para detectar

# ✅ Variáveis de controle para saber se os olhos estão sendo detectados e contar o tempo
tempo_ausente = 0            # Vai armazenar o tempo em que os olhos não foram detectados
olhos_detectados = True      # Estado inicial, assumindo que os olhos estão na tela

# ✅ Captura de vídeo da webcam (0 significa a câmera principal do computador)
cam = cv2.VideoCapture(0)

# ✅ Loop infinito para capturar os frames da câmera
while True:
    ok, frame = cam.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultado = face_mesh.process(rgb)

    if resultado.multi_face_landmarks:
        for face_landmarks in resultado.multi_face_landmarks:
            for i in [33, 133, 362, 263]: 
                ponto = face_landmarks.landmark[i]
                h, w, _ = frame.shape
                x, y = int(ponto.x * w), int(ponto.y * h)   
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
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

    cv2.imshow("Detecção de Olhos", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()