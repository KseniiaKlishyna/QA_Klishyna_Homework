from sqlalchemy.orm import declarative_base
from sqlalchemy import  VARCHAR, Integer, Column
import pytest
from sqlalchemy.orm import session



Base = declarative_base()

@pytest.fixture(autouse=True)
def truncate_table(request):
    yield
    session.execute('TRUNCATE TABLE tablewithusers;')
    session.commit()

class Users(Base):

    __tablename__ = 'tablewithusers'
    id = Column(VARCHAR(8), primary_key=True)
    first_name = Column(VARCHAR(25))
    last_name = Column(VARCHAR(25))
    age = Column(Integer)
    email = Column(VARCHAR(255))




