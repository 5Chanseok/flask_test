# 어플리케이션 구동
    - flask 명령상 기본으로 찾는 파일 (아래 파일들은 공존하면 의도치 않은 것이 수행될 수 있다.)
        - 1 개만 설정해야 한다.
        - wsgi.py
        - app.py
        - 환경 변수에 지정된 파일을(FLASK_APP=xxx) 찾는다.
    - 커스텀 설정
        1. 환경 변수를 지정하고 실행 -> OS에 설정하거나 혹은 shell(Mac/Linux) or cmd(Window) 작성해서 구동
            - set FLASK_APP=start_app
            - flask run

        2. 환경 변수 파일을 읽어서 처리
            - conda install python-dotenv -y
            - pip install python-dotenv
            - 파일 생성
                - env.config
                - start_app.py
            - 실행
                - flask -e ./env_config run

        3. 명령 수행 시 옵션 제공 -> 엔트리를 직접 지정하는 방식
            - flask --app start_app run
            - flask --app start_app --debug run

# 실습
    - wsgi.py 파일 생성
        - 명령어 flask run 으로 실행 ----> wsgi.py와 app.py 중 wsgi.py가 우선으로 실행된다.
        '''
            * Debug mode: off
            WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
            * Running on http://127.0.0.1:5000
            Press CTRL+C to quit
            127.0.0.1 - - [27/Mar/2023 10:24:35] "GET / HTTP/1.1" 200 -
        '''