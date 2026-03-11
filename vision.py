import cv2
import numpy as np

def init_camera():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        print("Erro ao abrir câmera")
        return None

    return cap

def detect_aruco(cap):

    ret, frame = cap.read()

    if not ret:
        return None

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()

    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    corners, ids, _ = detector.detectMarkers(gray)

    if ids is not None:
        print(f"Detectado ID: {ids[0][0]}")
        return ids[0][0]

    return None