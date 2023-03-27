# 사용자가 정의한(커스텀) 엔트리 포인트
# service를 대변하는 init 파일이다.
from flask import Flask

'''
    create_app은 플래스크 내부에서 정의된 함수명(수정 X)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()를 찾는다.
    차후 다른 모듈에서는 flask.current_app 이라는 변수로 app을 접근할 수 있다.(모듈 가져오기)
'''

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'home page 커스텀'
    
    return app

