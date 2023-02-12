#!/usr/bin/python3
"""
This module defines a unittest class for BaseModel class
of the file base_model.py
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """This is the unittest class for BaseModel class."""

    def setUp(self):
        self.base = BaseModel()

    def test_date_type(self):
        self.assertTrue(isinstance(self.base.created_at, datetime))
        self.assertTrue(isinstance(self.base.updated_at, datetime))
        self.assertFalse(isinstance(self.base.created_at, str))

    def test_uuid(self):
        with self.assertRaises(ValueError):
            uuid_obj = uuid.UUID(self.base.id, version=4)
            if uuid_obj:
                raise ValueError

    def test_dates(self):
        self.assertFalse(self.base.created_at > datetime.now())
        self.assertFalse(self.base.updated_at < self.base.created_at)

    def test_to_dict(self):
        dict_form = self.base.to_dict()
        self.assertIn('__class__', dict_form.keys())
        self.assertIn('BaseModel', dict_form.values())

    def test_compare_dict_object(self):
        dict_form = self.base.to_dict()
        self.assertEqual(self.base.id, dict_form['id'])
        self.assertTrue(
            self.base.created_at == datetime.fromisoformat(
                    dict_form['created_at']
                    )
            )

    def test_create_from_dict(self):
        self.base.name = "Holberton"
        base_copy = BaseModel(**self.base.to_dict())
        self.assertEqual(self.base.id, base_copy.id)
        self.assertEqual(self.base.created_at, base_copy.created_at)
        self.assertEqual(base_copy.name, "Holberton")
