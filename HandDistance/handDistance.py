import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Inicializa a camera
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Formata as dimensões da camera 3 sendo largura e 4 sendo altura definida em pixels
video.set(3, 1280)
video.set(4, 720)

while True:
    
    check, img = video.read()
    
    cv2.imshow('i',img)
    cv2.waitKey(1)
    
    