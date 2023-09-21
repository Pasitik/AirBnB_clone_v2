#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table(
    "place_amenity", Base.metadata,
	Column("place_id", String(60), ForeignKey("places.id", nullable=False))
	Column("amenity_id", String(60), ForeignKey("amenities.id"), nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="place")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates='place_amenities')

    

    @property
    def reviews(self):
        review_list = []
        for review in reviews:
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        amen = storage.all(Amenity)
        am_list[]
        for a in amen.values():
            if a.id is in self.amenity_id:
                am_list.append(a)
	        
        return sm_list;

    @amenities.setter
    def amenities(self, obj):
        '''adding an Amenity.id to the attribute amenity_ids'''
        if obj is not None and isinstance(obj, Amenity):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
