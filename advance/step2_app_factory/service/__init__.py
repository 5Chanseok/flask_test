# 사용자가 정의한(커스텀) 엔트리 포인트
# service를 대변하는 init 파일이다.
from flask import Flask
# TODO: ORM을 위한 추가
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
'''
    create_app은 플래스크 내부에서 정의된 함수명(수정 X)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()를 찾는다.
    차후 다른 모듈에서는 flask.current_app 이라는 변수로 app을 접근할 수 있다.(모듈 가져오기)
'''

def create_app():
    app = Flask(__name__)

    # 환경변수 초기화
    init_environment(app)
    # 데이터베이스 초기화
    init_database(app)
    # 블루프린트 초기화
    init_blueprint(app)
    
    return app

def init_environment(app):
    # 특정 파일(cfg, ..) 등을 읽어서 처리 가능
    app.config.from_pyfile('resource/config.cfg', silent=True)
    # py를 모듈 가져오기 해서 (객체)를 세팅해서 처리
    import service.config as config
    app.config.from_object(config)
    # 환경 변수(OS 레벨, flask 레벨, 사용자 정의 레벨) 모두 출력
    print('\n' + '-'*20)
    # 개별 환경 변수값 추출
    print(app.config['SECRET_KEY'], app.config.get('SECRET_KEY'))
    # for k, v in app.config.items() :
    #     print(k, v)
    print('-'*20 + '\n')
    pass

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

def init_database(app):
    # pool
    from .model import pool_sql
    pool_sql.init_pool()
    # 테스트
    print(pool_sql.login('guest', '1234'))
    # ORM을 위한 flask 객체와 sqlalchemy 객체, migrate 객체 연결
    db.init_app(app)
    migrate.init_app(app, db)
    # from .model import models
    