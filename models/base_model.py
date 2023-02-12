#!/usr/bin/python3
"""This module defines a class called BaseModel that is as
the parent class of others models.
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class defines all common attributes and methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """This is the constructor method of the class.
        args is not used in the constructor;
        On the other hand, kwargs is used to create a new BaseModel base on
        a dictionary object.
        Args:
            args: a variable length of non-keyworded arguments
            kwargs: a variable length of keyworded arguments
        """
        if kwargs and kwargs != {}:
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            for key in kwargs.keys():
                if not key in ('__class__', 'created_at', 'updated_at'):
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """The string representation method of the class.
        Return:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method updates the public instance attribute updated_at with
        the current datetime.
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the class to a dictionary with its attributes.
        """
        keys_values = {}
        keys_values['__class__'] = self.__class__.__name__
        keys_values['created_at'] = self.created_at.isoformat()
        keys_values['updated_at'] = self.updated_at.isoformat()
        for key, value in self.__dict__.items():
            if not key in keys_values.keys():
                keys_values[key] = value
        return keys_values
