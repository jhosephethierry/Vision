import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False

# Lendo a câmera e inicializando as solução
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)

# Coletar o tamanho da nossa tela
tela_w, tela_h = pyautogui.size()

# Coletar especificações da nossa câmera
_, frame = cam.read()
frame_h, frame_w, _ = frame.shape

# Loop principal
while True:
    
    # Flipando imagem
    _, img = cam.read()
    img = cv2.flip(img, 1)
    
    # Convertendo BGR para RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Coletando e Armazenando resultados
    results = face_mesh.process(rgb_img)
    landmark_points = results.multi_face_landmarks
    
    # Checando se existem os landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        
        # Identificando pontos necessários
        iris_and_mouth = [landmarks[145], landmarks[159], landmarks[14], landmarks[13]]
        
        # Checando se a boca está aberta
        distancia_da_boca = iris_and_mouth[-2].y - iris_and_mouth[-1].y
        
        # Manipulando
        if distancia_da_boca > 0.04:
            # Ignorar código do mouse
            pass
        else:
            pass
        
        # Iterando landmarks rosto
        for lm in landmarks:
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            
            # Desenhando landmarks
            cv2.circle(img, (x,y), 1, (255,0,255))
        
        # Iterando landmarks necessários    
        for lm in iris_and_mouth:
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            
            # Desenhando landmarks
            cv2.circle(img, (x,y), 4, (255,255,0))
    
    # Mostrando Visão
    cv2.imshow('Visao', img)
    
    # Esperando a tecla "q" pra encerrar o programa
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break