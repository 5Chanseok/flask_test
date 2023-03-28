'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''
from flask import render_template, request, url_for, jsonify
from service.controllers import bp_auth as auth
# 시간 정보를 획득, 시간차를 계산하는 함수
from datetime import datetime, timedelta
# Flask 객체 획득
from flask import current_app
import jwt

@auth.route('/')
def home():
    # 별칭.함수명 => url_for(앞의 내용 기입) => url이 리턴된다.
    print(url_for('auth_bp.login'))
    return "auth 홈"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # jwt 관련 체크 => 정상(200), 오류(401)
        # 1. uid, upw 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        # 2. uid, upw로 회원이 존재하는지 체크 -> (원래 디비, 임시로 값 비교)
        if uid=='guest' and upw=='1234':
            # 3. 회원이면 토큰 생성 (규격, 만료 시간, 암호 알고리즘 지정, ...)
            payload = {
                # 저장할 정보는 알아서 구성(고객 정보가 기반이기 때문)
                'id':uid,
                # 만료 시간(원하는데로 설정)
                'exp':datetime.utcnow() + timedelta(seconds=60*60*24)
                }
            # 토큰 발급 => 시크릿키, 해시 알고리즘("HS256"), 데이터(payload)
            SECRET_KEY = current_app.config['SECRET_KEY']   # 환경 변수값 획득
            # 발급
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            # 4. 응답 전문 구성 -> 응답
            return jsonify({'code':1, 'token':token})

@auth.route('/logout')
def logout():
    return "auth logout"

@auth.route('/signup')
def signup():
    return "auth signup"

@auth.route('/delete')
def delete():
    return "auth delete"