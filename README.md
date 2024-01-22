# PersonalColor
Personal color diagnosis

퍼스널 컬러 진단


## Usage

`git clone` 을 해 소스코드를 다운로드 해 주세요.


터미널에 `python color.py`을 입력하시면 웹캠 화면이 뜹니다.

키보드 자판의 `c`를 누르시면 캡쳐가 되고, 진단이 시작됩니다. 

추출된 히스토그램 결과값들을 확인 후 창을 닫아 주시면 터미널 창에 진단된 퍼스널 컬러가 나오게 됩니다.

> (피부값 추출 문제 있습니다.)

이후 `q`를 누르시면 진단 프로그램을 중단시킬 수 있습니다.



## 상세

`shape_predictor_68_face_landmarks.dat` 를 사용하는 `detect_face.py`에는 DetectFace 클래스가 있으며, 얼굴 감지 기능, 정확한 얼굴 부분 및 좌표를 제공합니다. 퍼스널컬러 분석을 위해 뺨, 눈, 눈썹 (머리카락 대신)을 선택했습니다.

`color_extract.py` 에는 DominantColors 클래스가 있으며 RGB 값을 사용하여 k-means clustering 알고리즘으로 대표 색상을 제공합니다. [이곳](https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036)에서 얻은 소스 코드를 수정했습니다.

RGB 값은 Lab 및 HSV 색 공간으로 변환됩니다. Lab의 b 값은 따뜻한 / 차가움을 결정하는 요소이고 HSV의 S 값은 봄 / 가을 또는 여름 / 겨울을 결정하는 요소입니다. 여러 이미지의 색상 값 데이터 세트를 분석하여 퍼스널 컬러를 분류하는 기준 값을 얻었습니다.
`tone_analysis.py` 는 퍼스널 컬러 분류를 위한 소스 코드입니다.

