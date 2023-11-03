import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from functools import lru_cache

import psycopg
from psycopg_pool import ConnectionPool, AsyncConnectionPool

load_dotenv()

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['DATABASE_USER']}:@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

conninfo = f"user={os.environ['DATABASE_USER']} password={os.environ['DATABASE_PASSWORD']} host={os.environ['DATABASE_HOST']} port={os.environ['DATABASE_PORT']} dbname={os.environ['DATABASE_NAME']}"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    with Session(engine) as session:
        yield session

        from functools import lru_cache


def get_conn():
    return psycopg.connect(conninfo=conninfo)


@lru_cache()
def get_pool():
    return ConnectionPool(conninfo=conninfo)


@lru_cache()
def get_async_pool():
    return AsyncConnectionPool(conninfo=conninfo)