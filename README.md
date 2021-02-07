# ILGIDAQ_Backend

가상환경 미포함.
필요한 앱: django, djangorestframework, Pillow
requrements로 만들자 필요한거
런칭할땐 settings.py/ALLOWED HOST에서 로컬호스트랑 아마존 지우고, DEBUG도 False로 하도록하도록합시다.

20210130: Develop 시작
20210202: settings.py/ALLOWED HOST 내용 추가. ilgidaq.nonok.ml에서 접속 및 로컬호스트 명시. 
            master에 넣을땐 로컬호스트 내용 지우는게 맞겠지?
            
20210208: feature/nonok/Response -> Develop
diaryMeta, diaryImage, diaryContent의 오류 상황에 대한 response 정리. API LIST 업데이트 했으니 참고 바람