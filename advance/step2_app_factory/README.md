# 어플리케이션 팩토리
    - 엔트리 위치 조정, 코드 조정
    - app = Flask(__name__)
        - 현재 이 코드는 전역변수로 존재
        - 프로젝트 규묘가 커지면, 순환 참조 할 확률이 높다.
        - flask 구현 시 어플리케이션 팩토리라는 형태로 사용하라 => 권장

# 방법
    - 플라스크 객체를 생성하는 코드를
        - 특정 패키지 밑에 위치 => ex) survice
        - __init__.py 로 이름 변경
        - 구조
            service
            L __init__.py
        - 최종 실행 명령
            - flask --app service --debug run

# 블루프린트
    - URL과 함수의 매핑(라우트)을 관리하는 도구

# 부트스트랩 <-> 머터리얼, ...
    - 부트스트랩 적용, 베이스 페이지 구성
        - https://getbootstrap.kr/docs/5.2/getting-started/download/
            - 다운로드 클릭 -> 압축 해제
            - static 폴더 하위에 파일 위치
                - bootstrap.min.css(or js)
        - https://getbootstrap.kr/docs/5.2/examples/
            - 다양한 UI 형태 예시로 제공

    - 디자인 적용 기준 설정
        - static 밑에 공통으로 사용할 CSS(부트스트랩) 적용
            - SASS 사용하는 회사도 존재 > CSS -> SASS로 넘어간느 추세
    - flask-bootstrap -> 2017 년 이후로 업데이트 X
        - 부트스트랩 버전 3.x => 사용 안함

# 입력폼의 유효성 검사 및 비정상적인 루트로 접근 시 처리 방지
    - 웹 프로그램에서 폼(FORM)은 사용자에게 입력 양식을 편리하게 제공
    - 폼 모듈을 활용해서 데이터 입력의 필수 여부, 길이, 형식, 유효성, 컨트롤 가능
    - flask-wtf
        - pip install flask-wtf
        - 기본 구성
            - SECRET_KEY 필수 구성
            - CSRF(cross-site request fogery)라는 웹 사이트 취약점 공격을 방지할 때 사용한다.
                - CSRF : 사용자의 요청을 위조하여 웹 사이트를 공격하는 기법
            - CSRF 토큰을 웹 페이지를 내려줄 때 삽입해서 요청이 들어올 때 그 값이 같이 요청을 타고 들어오게 처리
                - 이 값이 요청에 존재하는 경우(값 자체도 유효해야 함) 정상적인 루트로 진입했음을 인지한다.
                - <input type="hidden" name="" value=""> 이 패턴을 잘 체크
                - SECRET_KEY 값을 기반으로 해싱해서 토큰을 생성함
                    - 웹상에서 가장 잘 지켜야할 정보 => SECRET_KEY를 잘 관리해야 한다.

    - 실습
        - 환경 설정(변수)를 세팅해서 SECRET_KEY를 관리
        - 방식
            - OS 레벨에서 설정
            - 파이썬 객체로 설정 (O)
            - 환경 변수 파일로 설정
                - 플라스크 객체가 로드하면서 세팅 (O)
                - 플라스크를 가동하면서 세팅
                - 키값, 디비 연결값 등이 환경 변수로 빠질 것이다.
        - 질문폼 페이지 생성
            - url : ~/main/question, get 방식
            - html : question.html
                - base를 상속 받아서 내부는 div로만 감싸준다.

# JWT 개요
    - JSON Web Tokens
    - 토큰 기반 인증 방식
    - 왜 나왔고, 기존 대비 어떤 점이 유리한 지는 2 단계 기술 시 표현할 예정
    - 세션에 고객 정보를 담아서 보관하지 않고 고객의 필요한 정보를 토큰에 저장해서 클라이언트가 보관
        - (고급으로 가면 방식에 따라서 서버 측에도 디비 보관), 이를 증명서로 확인한다.(요청이 왔을 때 권한이 있는지 점검)
    - 구성
        - header    : 헤더, jwt 토큰 유형, 해시 알고리즘 사용 정보 기록(RSA, SHA256, ..)
        - payload   : 저장할 정보 => 클라이언트 정보, meta data, ...
        - signature : 서명, 헤더에서 지정한 알고리즘으로 + 플라스크의 시크릿키를 재료로 서명을 생성한다.(체크성 용도)
    - 위험 요소
        - 해커는 서버 측의 시크릿키를 탈취하면, jwt 정보를 해킹할 수 있다.
        - 인증서의 시간이 길면(만료 시간) 해독의 확률이 높아진다. -> 기한을 짧게 구성
            -> 기한을 짧게 구서하면 사용자는 빈번하게 로그인 해야한다. -> 불편함, 오버헤드(서버 측)
                -> 만료 시간을 연장하는 전략 or 리플레시 토큰을 서버 측에 저장해서 이를 기반으로 토큰 기간을 갱신하는 전략
                    -> 2 단계 진행
    - 설치
        - pip install PyJWT bcrypt

# TODO 주석 활용
    - TODO: 내용
        - 해야 할 작업
    - FIXME: 내용
        - 오작동, 버그 발생되는 코드
    - HACK: 내용
        - 해결은 했으나, 우아하거나 깔끔하지는 않다.(개선의 여지)
    - XXX: 내용
        - 이 부분은 큰 문제점/오류를 가지고 있다.

# 데이터베이스 연동
    - pool(풀링 기법)
        - 백엔드 서버가 가동하면, 백엔드와 데이터베이스 간 일정량의 커넥션을 미리 맺어서 큐(Queue:먼저 들어간 데이터가 먼저 나온다.)구조로 담아서 관리
        - 접속과 해제라는 반복 작업에 따른 으답 시간 지연 원인을 제거, 일정량의 동접이 발생했을 때, 안정적인 처리 속도를 제공
        - sqlalchemy
    - ORM 방식
        - 객체 지향 방식으로 코드에서 데이터베이스 연동, 데이터 처리 등을 관리
        - 원칙적으로는 SQL을 몰라도 처리 가능
            - 데이터베이스 벤더가 교체되더라도 동일하게 작동
        - 단점
            - 쿼리가 최적화 되었다고 볼 수 없다. -> 기계적인 생성
        - sqlalchemy, flask-migrate
    - 설치
        - pip install sqlalchemy  flask-migrate
    - 코드 작성
        - 
        ```
            from flask_sqlalchemy import SQLAlchemy
            from flask_migrate import Migrate

            db = SQLAlchemy()
            migrate = Migrate()
            ...
            db.init_app(app)
            migrate.init_app(app, db)

            # ORM 처리를 위한 환경 변수 설정
            # 임의 설정 환경 변수
            DB_PROTOCAL = "mysql+pymysql"
            DB_USER     = "root"
            DB_PASSWORD = "12341234"
            DB_HOST     = "127.0.0.1"
            DB_PORT     = 3306
            DB_DATABASE = "my_db"        # 새로 만들, 이 서비스에서 사용한 데이터베이스 명

            # 이 환경 변수는 migrate가 필수로 요구하는 환경 변수
            SQLALCHEMY_DATABASE_URI=f"{DB_PROTOCAL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

            # sqlalchemy 추가 설정
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        ```
        - 데이터베이스 생성, 초기화
            - --app service 는 없어도 되는데, 이 앱은 app or wsfi로 시작하는 엔트리가 없어서 별도로 지정해야한다.
            - flask --app service db init
                - sqlite : 소형 데이터베이스, 스마트폰에 사용하는 DB 의 경우에는 데이터베이스 생성을 자동으로 해줌, 파일럿 형태에서 사용
                - mysql 같은 데이터베이스(케이스별로 상이)는 실제로는 생성 안됨.
            - 명령어를 입력하면 migration 폴더가 생성된다.(내부는 자동으로 만들어지는 구조이므로 관여하지 않는다. 단, versions 밑으로 수정할 때마다 새로운 버전의 DB 관련 내용이 생성된다.)
        - 모델(테이블) 생성, 변경
            - model > models.py 에 테이블 관련 내용 기술
            - service > __init__.py
                - from .model import models : 주석 해제, 신규 작성
            - flask --app service db migrate
            ```
                MariaDB [my_db]> show tables;
                +-----------------+
                | Tables_in_my_db |
                +-----------------+
                | alembic_version |
                +-----------------+
                1 row in set (0.001 sec)
            ```
        - 모델(테이블) 생성, 변경 후 데이터베이스에 적용
            - flask --app service db upgrade
        - 컨테이너 이미지 생성 시
            - 위의 명령들 세 개를 차례대로 수행해서 데이터베이스 초기화 및 생성 과정을 수행
    - 필요한 기능들 시뮬레이션
        - DBA는 sql문을 작성해서 쿼리 구현
        - ORM에서는 shell을 열어서 파이썬 코드로 구현
        - flask --app service shell
            - 질문 등록
                ```
                    >>> from service.model.models import Question, Answer
                    >>> from datetime import datetime
                    >>> q1 = Question(title="질문1", content="내용1", reg_date=datetime.now())   
                    >>> from service import db
                    >>> db.session.add(q1)
                    >>> db.session.commit()
                ```
            - 질문 조회
                ```
                >>> Question.query.all()
                [<Question 1>]
                >>> qs = Question.query.all()
                >>> qs[0]
                <Question 1>
                >>> qs[0].id
                >>> qs[0].title
                '질문1'
                1   
                >>> Question.query.get(1)
                <Question 1>
                # 내용 중에 '용' 문자열이 존재하면 다 가져오시오.
                # select * from question where content like '%용%';
                # %용, %용%, 용% <- 내용 검색
                >>> Question.query.filter(Question.content.like('%용%')).all()
                [<Question 1>]
                ```
            - 질문 수정
                ```
                    >>> q1 = Question.query.get(1)
                    >>> q1
                    <Question 1>
                    >>> q1.title
                    '질문1'
                    # 변경하고 싶은 부분은 수정하면 된다.
                    # update question set tilte='질문11111' where id=1;
                    >>> q1.title = '질문11111'
                    >>> db.session.commit()
                    >>> q1.title
                    '질문11111'
                ```
            - 질문 삭제
                ```
                    q1 = Question.query.get(1)
                    # delete from question where id=1;
                    db.session.delete(q1)
                    db.session.commit()
                ```
            - 답변 등록
                ```
                     # 질문 한 개를 찾고 -> 답변을 등록
                    a = Answer(question=q2, content="질문에 대한 답변입니다.", reg_date=datetime.now())
                    db.session.add(a)
                    db.session.commit()
                ```
            - 답변을 통해서 답변 찾기
                ```
                    a.question
                ```
            - 질문을 통해서 답변 찾기
                ```
                    # 역참조의 이름을 사용하여 답변들을 다 찾아온다.
                    q2.answer_set
                ```
            - 질문을 삭제하면 답변도 다 삭제되는가?
                ```
                    db.session.delete(q2)
                    db.session.commit()

                    # 답변의 참조 question_id 값만 무효화 되었다.
                    # 작성자가 서로 다르므로 삭제 권리는 없고 참조만 제거했다.
                    MariaDB [my_db]> select * from answer;
                    +----+-------------+-----------------------------------+---------------------+
                    | id | question_id | content                           | reg_date            |
                    +----+-------------+-----------------------------------+---------------------+
                    |  1 |        NULL | 질문에 대한 답변입니다.            | 2023-04-05 13:16:15 |
                    +----+-------------+-----------------------------------+---------------------+
                    1 row in set (0.000 sec)

                    # 본인 답변 삭제
                    >>> db.session.delete(a)  
                    >>> db.session.commit()
                    MariaDB [my_db]> select * from answer;
                    Empty set (0.000 sec)
                ```