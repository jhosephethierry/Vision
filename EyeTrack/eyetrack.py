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
    
    # Esperando a tecla "q"
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break