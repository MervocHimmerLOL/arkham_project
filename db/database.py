from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from db.models import Base

engine = create_engine("sqlite:///example.db", echo=True)
SessionLocal = sessionmaker(bind=engine)
metadata_obj = MetaData()
# Создание таблиц (вызывай один раз при старте)
Base.metadata.create_all(engine)
