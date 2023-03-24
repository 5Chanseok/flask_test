'''
    데이터베이스 접속 후 쿼리 수행
'''
import pymysql as my

connection = None
try:
    connection = my.connect(host        = 'localhost',
                            port        = 3306,
                            user        = 'root',
                            password    = '12341234',
                            database    = 'ml_db',
                            # 조회 결과는 [{}, {}, {}, ...] 이런 형태로 추출된다.
                            # 사용하지 않으면 [(), (), ...] 이런 형태로 나온다.
                            # cursorclass = my.cursors.DictCursor
                            )

    # 쿼리 수행
    # pymysql은 커서를 획득해 쿼리를 수행한다. -> rule이기 때문에 그냥 따라한다.
    # 1. 커서 획득
    # connection.cursor(my.cursors.DictCursor) 이 방식도 가능하다. 위의 커서 주석하고
    with connection.cursor() as cursor: # I/O or 입출력 형태는 평소에도 이렇게 해주자
        # 2. sql문 준비
        sql = '''
            SELECT
                uid, `name`, regdate
            FROM
                users
            WHERE
                uid='guest'
            AND
                upw='1234';
        '''
        # 3. sql 쿼리 수행
        cursor.execute(sql)
        # 4. 결과를 획득
        row = cursor.fetchone()
        # 5. 결과 확인 -> 튜플 -> 이름만 추출 -> 순서가 중요, 인덱싱 -> '게스트'
        #    튜플로 결과를 받는 것은 결과값의 순서가 바뀌지 않는다는 전제하에서 가능
        #    유연하게 대처하고 싶다면 -> 컬럼 순서가 변경 되던지, 쿼리문의 순서가 변경 되던지와 상관없이 대응
        #    순서 없는 자료 구조 -> 딕셔너리 !! => d3.py에서 딕셔너리를 활용한다.
        print(row[1])
        # _, name, _ = row
        # print(name)
        pass
except Exception as e:
    print('접속 오류', e)
else:
    print('접속시 문제 없었음')
finally:
    if connection:
        connection.close()
