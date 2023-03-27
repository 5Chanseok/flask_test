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

    init_blueprint(app)
    
    return app

def init_blueprint(app):
    # app에 블루프린트 객체를 등록한다.

    # 실습 ~~~/auth/ 접속 시 인증홈이라는 내용이 나오도록 auth 관련 블루프린트를 구성하시오

    # 블루프린트로 정의된 개별 페이지 관련 내용 로드 -> 땡겨주기만 해도 실행되어 메모리에 올라간다.(연동된다.)
    from .controllers import main_controller
    from .controllers import auth_controller

    # from service.controllers import bp_main
    # 이 위치에서는 service를 생략하고 표현 가능
    from .controllers import bp_main, bp_auth
    
    # 플라스크 객체 블루프린트 등록
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)
    pass