#!/usr/bin/python3
"""
This module defines a unittest class for 'User' class
of the file user.py from the module models
"""
import unittest
from models.user import User
from datetime import datetime
import uuid


class TestUser(unittest.TestCase):
    """This is the unittest class for BaseModel class."""

    def setUp(self):
        self.user = User()

    def test_date_type(self):
        self.assertTrue(isinstance(self.user.created_at, datetime))
        self.assertTrue(isinstance(self.user.updated_at, datetime))
        self.assertFalse(isinstance(self.user.created_at, str))

    def test_uuid(self):
        with self.assertRaises(ValueError):
            uuid_obj = uuid.UUID(self.user.id, version=4)
            if uuid_obj:
                raise ValueError

    def test_dates(self):
        self.assertFalse(self.user.created_at > datetime.now())
        self.assertFalse(self.user.updated_at < self.user.created_at)

    def test_to_dict(self):
        dict_form = self.user.to_dict()
        self.assertIn('__class__', dict_form.keys())
        self.assertIn('User', dict_form.values())

    def test_compare_dict_object(self):
        dict_form = self.user.to_dict()
        self.assertEqual(self.user.id, dict_form['id'])
        self.assertTrue(
            self.user.created_at == datetime.fromisoformat(
                    dict_form['created_at']
                    )
            )

    def test_create_from_dict(self):
        self.user.name = "Holberton"
        user_copy = User(**self.user.to_dict())
        self.assertEqual(self.user.id, user_copy.id)
        self.assertEqual(self.user.created_at, user_copy.created_at)
        self.assertEqual(user_copy.name, "Holberton")
