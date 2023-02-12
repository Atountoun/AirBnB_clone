#!/usr/bin/python3
"""
This module defines a unittest class for Amenity class
of the file amenity.py of models module
"""
import unittest
from models.amenity import Amenity
from datetime import datetime
import uuid


class TestAmenity(unittest.TestCase):
    """This is the unittest class for Amenity class."""

    def setUp(self):
        self.amenity = Amenity()

    def test_date_type(self):
        self.assertTrue(isinstance(self.amenity.created_at, datetime))
        self.assertTrue(isinstance(self.amenity.updated_at, datetime))
        self.assertFalse(isinstance(self.amenity.created_at, str))

    def test_uuid(self):
        with self.assertRaises(ValueError):
            uuid_obj = uuid.UUID(self.amenity.id, version=4)
            if uuid_obj:
                raise ValueError

    def test_dates(self):
        self.assertFalse(self.amenity.created_at > datetime.now())
        self.assertFalse(self.amenity.updated_at < self.amenity.created_at)

    def test_to_dict(self):
        dict_form = self.amenity.to_dict()
        self.assertIn('__class__', dict_form.keys())
        self.assertIn('Amenity', dict_form.values())

    def test_compare_dict_object(self):
        dict_form = self.amenity.to_dict()
        self.assertEqual(self.amenity.id, dict_form['id'])
        self.assertTrue(
            self.amenity.created_at == datetime.fromisoformat(
                    dict_form['created_at']
                    )
            )

    def test_create_from_dict(self):
        self.amenity.name = "Holberton"
        amenity_copy = Amenity(**self.amenity.to_dict())
        self.assertEqual(self.amenity.id, amenity_copy.id)
        self.assertEqual(self.amenity.created_at, amenity_copy.created_at)
        self.assertEqual(amenity_copy.name, "Holberton")
