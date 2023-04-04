# 풀링 기법 적용
import sqlalchemy.pool as pool
import pymysql as my
from flask import current_app

# 커넥션 풀을 관리하는 객체 (전역 변수)
db_pool = None

# 커넥션 처리 함수
def get_conn():
    c = my.connect(host='localhost', user='root', password='12341234', database='ml_db', cursorclass=my.cursors.DictCursor)
    return c 

# 풀링 생성 함수
def init_pool():
    global db_pool
    '''
        pool_size    : 현재 구성 상, 생성한 커넥션 수, 가장 작은 값(최소 단위)
        max_overflow : 물리적으로 버틸 수 있는 최대값으로 설정(최대 동시 처리 수)
    '''
    db_pool = pool.QueuePool(get_conn, max_overflow=10, pool_size=5)

# 로그인 처리
def login(uid, upw):
    row = None
    print('풀링에서 관리하는 커넥션 수', db_pool.size())
    # 커넥션 풀에서 커넥션 한 개를 빌려와서 -> 쿼리 수행 -> 반납
    # 1. 커넥션 획득
    conn =  db_pool.connect()
        # 2. 커서 획득
    with conn.cursor() as cursor:
        sql = '''
            select
                *
            from
                users
            where
                uid=%s and upw=%s
        '''
        cursor.execute(sql, (uid, upw))
        row = cursor.fetchone()
    # 3. 반납 -> 명시적으로 안해도 된다는 듯?? 근데 웬만하면 해라
    conn.close()
    print('풀링에서 관리하는 커넥션 수', db_pool.size())
    return row
    pass
