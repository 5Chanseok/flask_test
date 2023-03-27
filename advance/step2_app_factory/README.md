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