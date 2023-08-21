import cv2
import mediapipe as mp
import numpy as np
import time # Utilizar pra checar timerate

class VisionDetector:
    
    def __init__(self, mode: bool = False, number_hands: int = 2, model_complexity: int = 1, min_detector_confidence: float = 0.5, min_tracking_confidence: float = 0.5):
        
        # Parametros necessários pra inicializar o Hands
        self.mode = mode
        self.max_num_hands = number_hands
        self.complexity = model_complexity
        self.detection_con = min_detector_confidence
        self.tracking_con = min_tracking_confidence
        
        # Inicializando o Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_num_hands, self.complexity, self.detection_con, self.tracking_con)
        self.mp_draw = mp.solutions.drawing_utils
        
    def find_hands(self, img: np.ndarray, draw_hands: bool = True):
        
        # Correção de cor BGR em RGB
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Coletar resultados do processo das hands e analizar
        self.results = self.hands.process(img_RGB)
        if self.results.multi_hands_landmarks:
            for hand in self.results.multi_hands_landmarks:
                if draw_hands:
                    self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HANDS_CONNECTIONS)
        
        return img
    
    
        
if __name__ == '__main__':
    
    capture = cv2.VideoCapture(0)

    Detector = VisionDetector()
    
    while True:
        
        _, img = capture.read()
        
        # Aqui manipularemos o frame e retornar o frame com o desenho da mão
        img = Detector.find_hands(img)
        
        cv2.imshow("imagem do Thierry", img)
        
        if cv2.waitKey(20) & 0xff==ord('q'):
            break
    