#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import city
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from os import getenv
import models


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref=backref(
            "state", cascade="all, delete"))

    @property
    def cities(self):
        """getter cities"""
        from models.city import City
        objs = models.storage.all(City)
        my_list = []
        for i in objs.values():
            if i.state_id == self.id:
                my_list.append(i)
        return my_list
