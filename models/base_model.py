#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """BaseModel class definition

    Attributes:
        id (sqlalchemy String): BaseModel id
        created_at (sqlalchemy DateTime): creation datetime
        updated_at (sqlalchemy DateTime): last update datetime
    """
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
            if storage_type == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}"
        .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime
        and saves the instance to storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        for key in dict:
            if type(dict[key]) is datetime:
                dict[key] = dict[key].isoformat()
        if '_sa_instance_state' in dict.keys():
            del(dict['_sa_instance_state'])
        return dict

    def delete(self):
        """Deletes the current instance from storage (models.storage)
        by calling the delete method
        """
        from models import storage
        models.storage.delete(self)
