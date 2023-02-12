#!/usr/bin/python3
"""
This module defines a unittest class for City class
of the file city.py of models module
"""
import unittest
from models.city import City
from datetime import datetime
import uuid


class TestCity(unittest.TestCase):
    """This is the unittest class for City class."""

    def setUp(self):
        self.city = City()

    def test_date_type(self):
        self.assertTrue(isinstance(self.city.created_at, datetime))
        self.assertTrue(isinstance(self.city.updated_at, datetime))
        self.assertFalse(isinstance(self.city.created_at, str))

    def test_uuid(self):
        with self.assertRaises(ValueError):
            uuid_obj = uuid.UUID(self.city.id, version=4)
            if uuid_obj:
                raise ValueError

    def test_dates(self):
        self.assertFalse(self.city.created_at > datetime.now())
        self.assertFalse(self.city.updated_at < self.city.created_at)

    def test_to_dict(self):
        dict_form = self.city.to_dict()
        self.assertIn('__class__', dict_form.keys())
        self.assertIn('City', dict_form.values())

    def test_compare_dict_object(self):
        dict_form = self.city.to_dict()
        self.assertEqual(self.city.id, dict_form['id'])
        self.assertTrue(
            self.city.created_at == datetime.fromisoformat(
                    dict_form['created_at']
                    )
            )

    def test_create_from_dict(self):
        self.city.name = "Holberton"
        city_copy = City(**self.city.to_dict())
        self.assertEqual(self.city.id, city_copy.id)
        self.assertEqual(self.city.created_at, city_copy.created_at)
        self.assertEqual(city_copy.name, "Holberton")
