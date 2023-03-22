# 홈페이지 작성, 디버깅 모드, 포트 5000번, 홈페이지는 화면에 "Helloworld" 만 출력
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Helloworld'

if __name__=="__main__":
    # 웹 상에 기본 포트 : http => 80 => 생략 가능
    # 나중에 웹 서버(apache, nginx)와 연동
    app.run(debug=True, host='0.0.0.0', port=5000)     # host='0.0.0.0' => 서버에서 호스트 잡을 때 사용
    