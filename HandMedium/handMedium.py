import cv2
import mediapipe as mp
import time

cap  = cv2.VideoCapture(0)

# Criando objeto hands com a biblioteca do mediapipe
mp_hands = mp.solutions.hands

# Declarando variável hands
hands = mp_hands.Hands()

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
    
    
    cv2.imshow('Hand Tracking', image)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()