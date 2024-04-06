from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE = "postgresql://admin:admin@postgres-db:5432/fast-api-db"

engine = create_engine(
    SQL_ALCHEMY_DATABASE
)

session_local = sessionmaker(bind=engine)

Base = declarative_base()


def get_session():
    with session_local() as session:
        yield session