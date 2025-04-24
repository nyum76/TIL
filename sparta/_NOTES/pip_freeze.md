# pip freeze
```py
# 현재 작업 환경에 설치되어있는 패키지 리스트 모두 출력
pip freeze

# requirements.txt 등의 파일에 패키지 리스트 담기
pip freeze > requirements.txt

# 패키지 설치
# !! 패키지를 설치하고 싶은 가상환경 활성화
conda activate AI_8 # 예시로 AI_8 이라는 가상환경 활성화 후,

pip install -r requirements.txt # r : read

''' 이 코드 반환시 설치 완료됨!
Successfully installed Django-3.0.3 PyJWT-1.7.1 argparse-1.4.0 bcrypt-3.1.7 beautifulsoup4-4.8.2 bs4-0.0.1 cffi-1.14.0 chardet-3.0.4 django-cors-headers-3.2.1 idna-2.8 mysqlclient-1.4.6 powerline-shell-0.7.0 pycparser-2.19 requests-2.22.0 six-1.14.0 soupsieve-1.9.5 urllib3-1.25.8
'''
```

