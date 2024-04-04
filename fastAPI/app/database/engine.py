from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE = "postgresql://admin:admin@0.0.0.0:5435/fast-api-db"

engine = create_engine(
    SQL_ALCHEMY_DATABASE
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def get_session():
    with session_local() as session:
        yield session