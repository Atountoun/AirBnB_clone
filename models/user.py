#!/usr/bin/python3
"""
This module defines a class User that inherits form BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits from BaseModel.
    Attributes:
    email (str): the email of the user
    password (str): the password of the user
    first_name (str): the first name of the user
    last_name (str): the last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """The class constructor that calls the super class constructor"""
        super().__init__(*args, **kwargs)
