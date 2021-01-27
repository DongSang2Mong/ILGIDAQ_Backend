# ILGIDAQ_Backend

가상환경 미포함.
필요한 앱: django, djangorestframework, Pillow


2021 01 20: nonok
master추가. 아무것도 없는데 그냥 베이스임

2021 01 22: nonok
develop 0122 시작
users 앱 생성 - UserLoginInfo 모델 , UserProfile 모델 생성
diary 앱 수정
- 정규표현식 검사 부분 추가
- 이미지 삭제or수정시 기존 파일 삭제
- diary 앱에 대한 API LIST를 구글 드라이브에 업로드

gitignore에 ###nonok###으로 내용 더 넣음. 너도 해라 태환아
setting.py.INSTALLED_APPS += 'rest_framework'
urls.py랑 settings.py에 미디어 처리되는거 추가
안해도 되는건데 푸시 해보고 싶어서 해봄 ㅋㅋ

feature_nonok 시작,

나의 다이어리를 알까?
아니었어!

2021 01 21: nonok
UML다이어그램 수정
이미지 업로드하면 /media/다이어리키/이미지num 으로 저장