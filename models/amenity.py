#!/usr/bin/python3
"""
This module defines a Amenity class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity inherits from BaseModel with additionnal attributes.
    Attributes:
        name (str): the name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """The Amenity class constructor."""
        super().__init__(*args, **kwargs)
