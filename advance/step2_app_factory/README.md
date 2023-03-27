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