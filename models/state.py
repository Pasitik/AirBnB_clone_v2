#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __table__ = "states"
    name = Column(String(128), nullable(False))
    cities = Relationship("City", back_populate="state")
