# personal_color_analysis/detect_face.py

# 필요한 패키지 가져오기
from imutils import face_utils
import numpy as np
import dlib
import cv2
import matplotlib.pyplot as plt

class DetectFace:
    def __init__(self, image):
        # dlib의 얼굴 검출기 초기화
        # facial landmark 예측기 생성
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('../res/shape_predictor_68_face_landmarks.dat')

        # 얼굴 부위 검출을 위한 이미지
        self.img = image

        # 얼굴 부위 초기화
        self.right_eyebrow = []
        self.left_eyebrow = []
        self.right_eye = []
        self.left_eye = []
        self.left_cheek = []
        self.right_cheek = []

        # 얼굴 부위 검출 수행
        self.detect_face_part()

    def detect_face_part(self):
        # 흑백 이미지로 변환
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # 얼굴 검출
        rects = self.detector(gray, 1)

        if len(rects) > 0:
            shape = self.predictor(gray, rects[0])
            shape = face_utils.shape_to_np(shape)

            # 얼굴 부위 변수 설정
            self.right_eyebrow = self.extract_face_part(shape[17:22])
            self.left_eyebrow = self.extract_face_part(shape[22:27])
            self.right_eye = self.extract_face_part(shape[36:42])
            self.left_eye = self.extract_face_part(shape[42:48])
            # 뺨 부위는 얼굴 랜드마크와 상대적인 위치로 검출
            self.left_cheek = self.extract_face_part(shape[29:33])
            self.right_cheek = self.extract_face_part(shape[33:37])

    def extract_face_part(self, face_part_points):
        (x, y, w, h) = cv2.boundingRect(face_part_points)
        crop = self.img[y:y+h, x:x+w]
        adj_points = np.array([np.array([p[0]-x, p[1]-y]) for p in face_part_points])

        # 히스토그램 계산
        hist = cv2.calcHist([crop], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

        # Normalize the histogram
        hist = hist.flatten()
        hist = hist / hist.sum()

        return crop