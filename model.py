from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


Base = declarative_base()
engine= create_engine('sqlite:///tiendaDB.db')

class User(Base):
    __tablename__ = 'users'
    
    user=Column(String(50), unique=True, nullable=False, primary_key=True)
    password = Column(String(50), nullable=False)
    created_on=Column(DateTime(), default=datetime.now)
    update_on =Column(DateTime(), default=datetime.now, onupdate=datetime.now)

Base.metadata.create_all(engine)
Session= sessionmaker(bind=engine)
session= Session()

def searchUser(user:str)->bool:
    """
    Verifica si existe el usuario o no en la base de datos
    :param user: string con el nombre de usuario
    """
    return session.query(1).filter(User.user==user).first() and True
def searchPass(user:str, password:str)->bool:
    """
    Verifica si existe el usuario con su correspondiente contraseña
    o no en la base de datos
    :param user: string con el nombre de usuario
    :param user: string con la contraseña
    """
    return session.query(1).filter(User.user==user, User.password==password).first() and True

"""
user1= User(user="Emerson1", password="1234")
session.bulk_save_objects(
    [User(user="Shadow", password="1111"),
    User(user= "Jemima", password="2222"),
    User(user="Guillermo", password="3333")
])
session.commit()
"""

