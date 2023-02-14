#!/usr/bin/python3
"""
This module defines a file_storage class used for instances storage in file.
"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "City": City,
        "Review": Review,
        "Amenity": Amenity,
        "State": State
        }


class FileStorage:
    """Class used to serialize instances to a JSON file and deserialize JSON
    file to instances.
    Attributes:
        file_path (str): the path to the JSON file
        objects (dict): will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """The class constructor with no argument."""
        pass

    def all(self):
        """This method is used to retrieve data stored in class attribute
        'objects'
        Return:
            The dictionay __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """This method is used to add a new object to the class attribute
        'objects'
        Args:
            The new object to be added
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """This method is used to serialize class attributes 'objects' to
        the JSON file (path: class attribute 'file_path')
        """
        path = FileStorage.__file_path
        with open(path, 'w') as fd:
            data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(data, fd)

    def reload(self):
        """This method is used to deserialize the JSON file to class attribute
        'objects' (only if the JSON file exits), otherwisen do nothing.
        """
        path = FileStorage.__file_path
        if os.path.exists(path):
            with open(path, 'r') as fd:
                data = json.load(fd)
                for key in data.keys():
                    FileStorage.__objects[key] = classes[
                            data[key]["__class__"]](**data[key])
