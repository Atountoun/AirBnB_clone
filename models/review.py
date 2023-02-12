#!/usr/bin/python3
"""
This module defines a Review class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel with additionnal attributes.
    Attributes:
        place_id (str): the identifier of the place, Place.id
        user_id (str): the identifier of the user, User.id
        text (str): the review text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """The Review class constructor."""
        super().__init__(*args, **kwargs)
