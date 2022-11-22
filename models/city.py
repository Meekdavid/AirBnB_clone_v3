<<<<<<< HEAD
#!/usr/bin/python3
'''
    Define the class City.
'''
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
=======
#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
>>>>>>> main
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.state import State


class City(BaseModel, Base):
<<<<<<< HEAD
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
=======
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place",
                              backref="cities",
>>>>>>> main
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
>>>>>>> main
