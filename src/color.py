# webcam_color.py

import cv2
from personal_color_analysis import personal_color

def main():

    # 웹캠 사용
    cap = cv2.VideoCapture(0)

    while True:
        # 웹캠의 경우 프레임 읽기
        ret, frame = cap.read()
        if not ret or frame is None:
            continue

        # 화면 출력
        cv2.imshow("Input", frame)

        # 키 입력 대기
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("c"):
            # 개인 색상 분석 함수 호출
            personal_color.analysis(frame)

    # 웹캠이면 해제, 이미지 파일이면 창 닫기
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()