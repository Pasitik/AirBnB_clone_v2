#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id', String(60), ForeignKey('places.id'),
        nullable=False, primary_key=True
    ),
    Column(
        'amenity_id', String(60), ForeignKey('amenities.id'),
        nullable=False, primary_key=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    name = Column('name', String(128))
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    # amenity_id = Column(String(60), ForeignKey('amenities.id'))
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    # cities = relationship('City', backref=backref('place', uselist=False))
    # user = relationship('User',  back_populates='places')
    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False,
        back_populates='place_amenities',
    )

    # else:
    #     name = ""
    #     description = ""
    #     number_rooms = 0
    #     number_bathrooms = 0
    #     max_guest = 0
    #     price_by_night = 0
    #     latitude = 0.0
    #     longitude = 0.0
    #     city_id = ""
    # amenity_id = 0
    #     user_id = ""
