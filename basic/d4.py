'''
    데이터베이스 접속 후 쿼리 수행 + 파라미터 전달
'''
import pymysql as my

def select_login(uid, upw):
    '''
        아이디, 비밀번호를 넣어서 회원 여부를 체크하는 함수
        parameter
            - uid : 아이디
            - upw : 비밀번호
        returns
            - 회원인 경우
                - {'uid': 'guest', 'name': '게스트', 'regdate': datetime.datetime(2023, 3, 24, 13, 2, 26)}
            - 비회원인 경우, 디비측 오류
                - None
    '''
    connection = None
    row = None  # 로그인 쿼리 수행 결과를 담는 변수
    try:
        connection = my.connect(host        = 'localhost',
                                port        = 3306,
                                user        = 'root',
                                password    = '12341234',
                                database    = 'ml_db',
                                cursorclass = my.cursors.DictCursor
                                )

        with connection.cursor() as cursor:
            # 파라미터는 %s 표시로 순서대로 세팅된다. '값' => ''는 자동으로 세팅된다. '%s' 할 필요 없다.
            sql = '''
                SELECT
                    uid, `name`, regdate
                FROM
                    users
                WHERE
                    uid=%s
                AND
                    upw=%s;
            '''
            # execute() 함수의 2 번 인자가 파라미터 전달하는 자리, 튜플로 표현
            cursor.execute(sql, (uid, upw))
            row = cursor.fetchone()    # 결과 셋 중 한 개만 가져온다. -> 단수(리스트가 아닌 단독 타입 : 딕셔너리), fetall : 리스트로 나옴
            # print(row['name'])
            pass
    except Exception as e:
        print('접속 오류', e)
    else:
        print('접속시 문제 없었음')
    finally:  # 예외 상황이던 아니던 무조건 수행된다.
        if connection:
            connection.close()
    # 로그인한 결과를 리턴 -> {...} 딕셔너리 구조로 리턴
    return row

if __name__ == '__main__':
    # d4 개발자의 테스트 코드
    # f5 개발자가 사용할 때는 작동하지 않는다.
    # 정상 계정
    print(select_login('guest', '1234'))
    # 비정상 계정
    print(select_login('guest', '12345'))