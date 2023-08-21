import cv2
import mediapipe as mp
import time

cap  = cv2.VideoCapture(0)

# Criando objeto hands com a biblioteca do mediapipe
mp_hands = mp.solutions.hands

# Declarando variável hands
hands = mp_hands.Hands()

# Declarando variável para desenhar pontos nas mãos
mp_draw = mp.solutions.drawing_utils

# Declarando variáveis de tempo
p_time = 0
c_time = 0


while True:
    
    success, image = cap.read()
    
    # Converter imagem BGR para RGB
    img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resultado da imagem
    results = hands.process(img_RGB)
    
    # Imprimindo resultados no terminal
    print(results)
    
    # Imprimindo e checando detecção
    print(results.multi_hand_landmarks)
    
    # Se as marcas das mãos forem detectadas iniciar desenho dos pontos e conexões
    if results.multi_hand_landmarks:
        
        for hand_landmarks in results.multi_hand_landmarks:
            
            # Carregando e imprimendo indice das marcas
            for id, ln in enumerate(hand_landmarks.landmark):
                
                h, w, c = image.shape
                cx, cy = int(ln.x*w), int(ln.y*h)
                print(id, cx, cy)
                
            # Desenhando circulos nas pontas dos dedos
            if id == 4:
                cv2.circle(image, (cx,cy), 15, (255,7,255), cv2.FILLED)
            if id == 8:
                cv2.circle(image, (cx,cy), 15, (255,7,255), cv2.FILLED)
            if id == 12:
                cv2.circle(image, (cx,cy), 15, (255,7,255), cv2.FILLED)
            if id == 16:
                cv2.circle(image, (cx,cy), 15, (255,7,255), cv2.FILLED)
            if id == 20:
                cv2.circle(image, (cx,cy), 15, (255,7,255), cv2.FILLED)
                
    mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    # Declarando tempo corrido
    c_time = time.time()
    p_time = c_time
    fps = 1/(c_time * p_time)
    
    # Mostrando Quadro Chave
    cv2.putText(image, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,7,255), 3)
            
    
    cv2.imshow('Hand Tracking', image)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()