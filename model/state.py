#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

    # Check if storage engine is not DBStorage
    if storage_type != "db":
        @property
        def cities(self):
            """Getter method to return the list of City objects linked to the current State."""
            citiesList = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    citiesList.append(city)
            return citiesList
