from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


username = 'root'
password = 'Ksenia3012'
host = 'localhost'
port = 3306
database_name = 'mycooldb'


engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}')


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()





