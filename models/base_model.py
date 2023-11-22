#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """This class defines common attributes/methods for other classes"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        if not self.id:
            self.id = str(uuid.uuid4())
        time = datetime.utcnow()
        if not self.created_at:
            self.created_at = time
        if not self.updated_at:
            self.updated_at = time

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime
        and saves the instance to storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict.pop('_sa_instance_state', None)
        return new_dict

    def delete(self):
        """Deletes the current instance from storage (models.storage)
        by calling the delete method
        """
        models.storage.delete(self)
