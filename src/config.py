from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
db_name = os.getenv('DATABASE')

# Создайте движок для подключения к базе данных
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

Base = declarative_base()
