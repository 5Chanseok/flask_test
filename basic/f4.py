'''
    - GET 방식으로 데이터 전송하기
        - 클라이언트 (키=값&키=값...)
            - 링크 => 화면 전환
                <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a> --> 일반적인??

            - form 전송, 화면 껌벅 => 화면 전환
                <form action="http://127.0.0.1:5000/link" method="get">  action, method ==> 속성
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송">
                </form> ----> 합쳐서 엘리먼트라고 하고, 시작 종료 태그, 컨텐츠로 구성되어 있다. 사용자에게 입력을 받는 경우 활용, 가입 및 검색

            - ajax 가능 (jQuery로 함축적으로 표현), 화면은 현재 화면을 유지한다. 얘도 입력 받을 수 있는듯??
                $.get({
                    url:"http://127.0.0.1:5000/link",
                    data:"name=hello&age=100",
                    success:(res)=>{},
                    error:(err)={}
                })
        - 서버
            - get 방식 데이터 추출
            - name = request.args.get('name')
            - age  = request.args.get('age')
    - /link 쪽으로 요청하는 방식은 다양할 수 있다. 단 사이트 설계상 한 가지로만 정의되어 있다면
      다른 방식의 접근은 모두 비정상적인 접근이다.(웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링 할 것인가? 보안의 기본 사항
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/link')
def link():
    # request.args['age'] => 데이터 누락 시 서버 셧다운 된다. 사용하면 안된다.
    # age  = request.args.get('age') => 데이터 누락 시 None이 나와 예외 처리 가능
    name = request.args.get('name')
    age  = request.args.get('age')
    return "[%s] [%s] " %(name, age)

@app.route('/test')
def test():
    # 엔트리포인트(진입로, 프로그램 시작점)과 같은 경로에 templates/test.html 생성해야 에러 발생 X
    return render_template('test.html')

if __name__=="__main__":
    app.run(debug=True)
    