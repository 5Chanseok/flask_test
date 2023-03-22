# flask_test
practicing &amp; testing flask 


# 파이썬 기반 웹 프로그래밍

# 목표
    - 웹 환경 이해 및 웹 프로그램 구성 이해
    - flask 기반 웹 기반 백엔드(서버) 프로그래밍
    - blueprint를 이용한 기능별 분할 구성
    - 데이터 베이스 연동 (sql, ORM)
    - 배포 및 운영

# 발전적 목표
    - 머신러닝/딥러닝 모델 서빙 및 서비스 구현
    - 구축된 서비스를 도커 및 쿠버네티스 기반 하에서 운영
    - MLOps에 연동 사용

# 가상 환경 구축
    - 순수 파이썬
        - 가상 환경을 모아 두는 폴더 생성 
            - mkdir venvs (mkdir : make directory)
        - 해당 폴더로 이동 
            - cd venvs (cd : change directory)
        - 가상 환경 생성 
            - python -m venv web(가상 환경 이름)
        - 가상 환경 활성화 하는 명령어 위치까지 이동
            - cd ./web/Scripts
        - 가상 환경 활성화
            - Window
                - activate
            - Mac, Linux
                - . activate --> Mac 기준
        - 최종 프롬프트 형태
            - (web) >   <--- Window
            - (web) $   <--- Mac/Linux 사용자 계정 
            - (web) #   <--- Mac/Linux 루트 계정
    - 아나콘다(미니콘다, ....)

# 필요한 패키지 설치
    - requirements.txt 생성 ---> git에서 사용하는 모든 공개적인 프로젝트는 생성해야 한다.
    - 작성
        - 수동
            - 직접 기입 <--- 패키지 하나 올라갈 때마다 기입하는 것이 좋다.
            - 패키지==버전
            - 패키지 <--- 최신 버전을 의미
        - 자동 
            - 개발이 다 종료된 후 사용하는 것을 권장
                - 개발 중에 생성한다면
                    - 패키지가 이미 일부 설치가 혹은 전부 설치가 되어 있다.
                    - 내가 설치하지 않은 패키지도 추가된다.
            - pip freeze > requirements.txt

    - 설치
        - pip install -r requirements.txt