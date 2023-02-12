#!/usr/bin/python3
"""
This module defines a State class that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that inherits from BaseModel with additionnal attributes.
    Attributes:
        name (str): the name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """The class constructor."""
        super().__init__(*args, **kwargs)
