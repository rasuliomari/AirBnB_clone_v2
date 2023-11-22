#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
=======
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

>>>>>>> 8445836df0ae9d0885409c87b5607692e32809af


class User(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
=======
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
>>>>>>> 8445836df0ae9d0885409c87b5607692e32809af
