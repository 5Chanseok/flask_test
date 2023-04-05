SECRET_KEY='hynix'    # 서비스 시 추론이 불가한 해시값 추천

# 클레스를 정의해서 내부에 멤버로 표현해도 됨

# ORM 처리를 위한 환경 변수 설정
# 임의 설정 환경 변수
DB_PROTOCAL = "mysql+pymysql"
DB_USER     = "root"
DB_PASSWORD = "12341234"
DB_HOST     = "127.0.0.1"
DB_PORT     = 3306
DB_DATABASE = "my_db"        # 새로 만들, 이 서비스에서 사용한 데이터베이스 명

# 이 환경 변수는 migrate가 필수로 요구하는 환경 변수
SQLALCHEMY_DATABASE_URI=f"{DB_PROTOCAL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# sqlalchemy 추가 설정
SQLALCHEMY_TRACK_MODIFICATIONS=False