#!/usr/bin/python3
"""
    contains state class to represent a state
"""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import environ
from models.city import City
import shlex

#storage_engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class: class to represent states of cities"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all')

    @property
    def cities(self):
        #from models.city import City
        var = models.storage.all()
        listl = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                listal.append(var[key])
        for elem in listl:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
