import os
import sys
from logging.config import fileConfig
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

# .env 로드 (DATABASE_URL 등)
load_dotenv()

# Alembic Config 객체
config = context.config
fileConfig(config.config_file_name)

# asyncpg → psycopg2로 치환해서 동기 마이그레이션용 URL 생성
DATABASE_URL = os.getenv("DATABASE_URL").replace("asyncpg", "psycopg2")

# 모델 metadata 불러오기 (Base = DeclarativeBase)
from app.infrastructure.db.session import Base  # ✅ Base.metadata를 가져오기 위함
import app.infrastructure.db.models
target_metadata = Base.metadata


def run_migrations_online():
    """동기 엔진을 사용한 마이그레이션 실행"""

    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # 컬럼 타입 변경도 감지
        )

        with context.begin_transaction():
            context.run_migrations()


# 실행
run_migrations_online()
