import sqlalchemy
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///restaurant.db"
engine = create_engine(db_url)

Base = declarative_base()