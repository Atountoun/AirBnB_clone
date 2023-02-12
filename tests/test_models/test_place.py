#!/usr/bin/python3
"""
This module defines a unittest class for Place class
of the file place.py of models module
"""
import unittest
from models.place import Place
from datetime import datetime
import uuid


class TestPlace(unittest.TestCase):
    """This is the unittest class for 'Place' class."""

    def setUp(self):
        self.place = Place()

    def test_date_type(self):
        self.assertTrue(isinstance(self.place.created_at, datetime))
        self.assertTrue(isinstance(self.place.updated_at, datetime))
        self.assertFalse(isinstance(self.place.created_at, str))

    def test_uuid(self):
        with self.assertRaises(ValueError):
            uuid_obj = uuid.UUID(self.place.id, version=4)
            if uuid_obj:
                raise ValueError

    def test_dates(self):
        self.assertFalse(self.place.created_at > datetime.now())
        self.assertFalse(self.place.updated_at < self.place.created_at)

    def test_to_dict(self):
        dict_form = self.place.to_dict()
        self.assertIn('__class__', dict_form.keys())
        self.assertIn('Place', dict_form.values())

    def test_compare_dict_object(self):
        dict_form = self.place.to_dict()
        self.assertEqual(self.place.id, dict_form['id'])
        self.assertTrue(
            self.place.created_at == datetime.fromisoformat(
                    dict_form['created_at']
                    )
            )

    def test_create_from_dict(self):
        self.place.name = "Holberton"
        place_copy = Place(**self.place.to_dict())
        self.assertEqual(self.place.id, place_copy.id)
        self.assertEqual(self.place.created_at, place_copy.created_at)
        self.assertEqual(place_copy.name, "Holberton")
