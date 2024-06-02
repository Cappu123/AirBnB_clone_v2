#!/usr/bin/python3
"""
    contains City class to represent a city
    contains City class to represent a city
"""
from models.state import State
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer
from os import environ
from sqlalchemy.ext.declarative import declarative_base

#storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ City class :City class to represent a city
    City class :City class to represent a city
    """
    #from models.state import State
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id))
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities")
