from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# db_url = 'postgres:5432'
db_url = 'postgres'
db_name = 'properpulse'
db_user = 'postgres'
db_password = 'Pr0p3r-Pu1s3'
engine = create_engine(
    f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
# engine = create_engine(
#     f'postgresql+psycopg2://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by