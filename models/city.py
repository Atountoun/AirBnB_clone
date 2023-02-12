#!/usr/bin/python3
"""
This module defines a City class that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City inherits from BaseModel with additionnal attributes.
    Attributes:
        state_id (str): the identifier of the state of the city
        name (str): the name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """The City class constructor"""
        super().__init__(*args, **kwargs)
