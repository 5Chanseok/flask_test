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
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

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
        uid = request.form.get('name')
        upw = request.form.get('age')   # 암호는 차후에 암화화 해야한다.(관리자도 볼 수 없다. 해싱)
        print(uid, upw)
          # 2. 회원 여부 쿼리
          # 3. 회원이면
              # 3-1. 세션 생성, 기타 필요한 조치 수행
              # 3-2. 서비스 메인 화면으로 이동
          # 4. 회원 아니면
              # 4-1. 적당한 메시지 후 다시 로그인 유도
        return redirect('https://www.naver.com') # 요청을 다른 URL로 포워딩한다.

if __name__=="__main__":
    app.run(debug=True)
    