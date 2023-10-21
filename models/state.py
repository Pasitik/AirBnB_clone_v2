#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", back_populates="state")


    @property
    def cities(self):
        '''returns the list of City instances with state_id
           equals the current State.id
           FileStorage relationship between State and City
        '''
        from models import storage
        from models.city import City
        related = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                related.append(city)
        return related
