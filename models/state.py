#!/usr/bin/python3
<<<<<<< HEAD
'''
    Implementation of the State class
'''
from os import getenv
from sqlalchemy import Column, String
=======
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
>>>>>>> main
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
<<<<<<< HEAD
    '''
        Implementation for the State.
        Create relationship between class State (parent) to City (child)
    '''
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
=======
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
>>>>>>> main
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

<<<<<<< HEAD
        @property
        def cities(self):
            '''
                Return list of city instances if City.state_id==current
                State.id
                FileStorage relationship between State and City
            '''
            list_cities = []
            for city in models.storage.all("City").values():
=======
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
>>>>>>> main
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
