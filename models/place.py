#!/usr/bin/python3
""" Place Module for HBNB project """
import uuid
from datetime import datetime

"""# Import required modules modules and classes"""
#from models.review import Review
#from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy import *
import os
import models

"""
# Define a table to represent the many-to-many
# relationship between Place and Amenity.
"""
_metadata = Base.metadata
place_amenity = Table('place_amenity', _metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))

"""# Define the Place class"""
class Place(BaseModel, Base):
    """
    This is a class for a Place in Airbnb
    """

    __tablename__ = 'places'

    """# Define columns in the 'places' table"""
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    """
    # Check the storage type and define relationships accordingly
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        """
        # Relationships for database storage using SQLAlchemy's ORM"""
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        """
        # Property methods for file storage
        """
        @property
        def reviews(self):
            my_list = []
            for key, val in models.storage.all(Review).items():
                if val.place_id == self.id:
                    my_list.append(val)
            return my_list

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
