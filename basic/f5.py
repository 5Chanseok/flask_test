'''
    - POST 방식으로 데이터 전송하기
        - 클라이언트 (json, Xml, Text, Form, Form-encode(키=값&키=값...), Graphql, Binary
            - form 전송, 화면 껌벅 => 화면 전환, (Form, Form-encode 형식)
                <form action="http://127.0.0.1:5000/link" method="post">  action, method ==> 속성
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송">
                </form> ----> 합쳐서 엘리먼트라고 하고, 시작 종료 태그, 컨텐츠로 구성되어 있다. 사용자에게 입력을 받는 경우 활용, 가입 및 검색

            - ajax 가능 (jQuery로 함축적으로 표현), 화면은 현재 화면을 유지한다. 얘도 입력 받을 수 있는듯??
                - (json, Xml, Text, Form, Form-encode(키=값&키=값...), Graphql, Binary) 방식 가능
                $.pest({
                    url:"http://127.0.0.1:5000/link",
                    data:"name=hello&age=100",
                    success:(res)=>{},
                    error:(err)={}
                })
        - 서버
            - post 방식 데이터 추출
            - name = request.form.get('name')
            - age  = request.form.get('age')
    - /link 쪽으로 요청하는 방식은 다양할 수 있다. 단 사이트 설계상 한 가지로만 정의되어 있다면
      다른 방식의 접근은 모두 비정상적인 접근이다.(웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링 할 것인가? 보안의 기본 사항
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from d4 import select_login

app = Flask(__name__)
# 세션을 위해 시크릿 키 지정
app.secret_key = 'ckstjr95'     # 임의값, 통상적으로 해시값 활용

# 로그인을 하여 세션을 얻은 후 홈페이지를 진입해야 사이트의 내용을 보여주겠다. => 컨셉
@app.route('/')
def home():
    if not 'uid' in session: # 세션 안에 uid 값이 존재하는가?
        # return redirect('/login') # ---> url을 사용할 때는 하드코딩 하지 않는다.
        # url_for('사용하고자 하는 url과 연결된 함수명을 기입')
        return redirect(url_for('login'))
    return "helloworld"

# @app.route() => 기본적으로 get 방식
# method 추가 => methods=['POST', ...]
@app.route('/login', methods=['POST', 'GET'])
def login():
    # method별 분기
    if request.method == 'GET':
        return render_template('login.html')
    else: # post
          # request.form['uid'] ---> 값이 누락되면 서버 셧다운, 사용 금지
          # 1. 로그인 정보 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')   # 암호는 차후에 암화화 해야한다.(관리자도 볼 수 없다. 해싱)
        print(uid, upw)
          # 2. 회원 여부 쿼리
        result = select_login(uid, upw)
        if result:  # 3. 회원이면
              # 세션 : 클라이언트 정보를 서버가 메모리 상에 유지해서 클라이언트가 간편하게 웹을 이용할 수 있도록 도움을 줌
              #        단점 : 접속 유저가 많으면 서버 측 메모리에 부하가 온다. -> 대체제/대안 필요
              #        -> JWT 를 사용하여 보완(사이트 구성 시 인증 쪽에서 활용 : 차주 진행한다.)
              # 3-1. 세션 생성, 기타 필요한 조치 수행
            session['uid'] = uid
              # 3-2. 서비스 메인 화면으로 이동
            return redirect(url_for('home'))
            pass
        else:  # 4. 회원 아니면

              # 4-1. 적당한 메시지 후 다시 로그인 유도
            # render_template() => jinja2 템플릿 엔진을 사용한다. -> 문법도 jinja2 문법으로 해줘야 한다.
            return render_template('error.html', msg='로그인 실패')
            pass
        # return redirect('https://www.naver.com') # 요청을 다른 URL로 포워딩한다.

if __name__=="__main__":
    app.run(debug=True)
    