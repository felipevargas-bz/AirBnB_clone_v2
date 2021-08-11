#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base



class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = ""
    name = Column(String(60), primary_key=True, nullable=False)
