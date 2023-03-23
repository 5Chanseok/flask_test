'''
    라우트 추가 -> URL 추가
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# 기획서를 기반하여 총 페이지 수 만큼 URL 준비 -> 뼈대부터 준비한다.
# 뼈대를 먼저 잡아서 각 페이지에 해당하는 URL 준비
# blueprint를 사용한다면, 대분류, 중분류(생략 가능), 소분류 같은 트리 구조로 배치
# /login <-> blueprint 활용 : /auth/users/login

@app.route('/')
def home():
    return 'Helloworld'

# 아래와 같은 url 구성은 blueprint를 사용하여 섹션을 나눠 관리하는 것이 더 낫다.
@app.route('/auth/users/login')
def login():
    return 'login page'

@app.route('/auth/users/signup')
def signup():
    return 'signup page'

if __name__=="__main__":
    app.run(debug=True)
    