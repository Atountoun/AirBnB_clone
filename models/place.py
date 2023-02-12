#!/usr/bin/python3
"""
This module defines a Place class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class inherits from BaseModel with additionnal attributes.
    Attributes:
        city_id (str): the identifier of the city of the place, City.id
        user_id (str): the identifier of the user, User.id
        name (str): the name of the place
        description (str): the description of the plae
        number_rooms (int): the number of rooms of the place
        number_bathrooms (int): the number of bathrooms of the place
        max_guest (int): the maximal number of guests of the place
        price_by_night (int): the place of the place by night
        latitude (float): the latitude value of the place
        longitude (float): the longitude value of the place
        amenity_ids (list(str)): the amenities of the place, list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """The Place class constructor."""
        super().__init__(*args, **kwargs)
