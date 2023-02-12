#!/usr/bin/python3
"""
This module defines a unittest class for State class
of the file state of models module
"""
import unittest
from models.state import State
from datetime import datetime
import uuid


class TestState(unittest.TestCase):
    """This is the unittest class for State class."""

    def setUp(self):
        self.state = State()

    def test_date_type(self):
        self.assertTrue(isinstance(self.state.created_at, datetime))
        self.assertTrue(isinstance(self.state.updated_at, datetime))
        self.assertFalse(isinstance(self.state.created_at, str))

    def test_uuid(self):
        with self.assertRaises(ValueError):
            uuid_obj = uuid.UUID(self.state.id, version=4)
            if uuid_obj:
                raise ValueError

    def test_dates(self):
        self.assertFalse(self.state.created_at > datetime.now())
        self.assertFalse(self.state.updated_at < self.state.created_at)

    def test_to_dict(self):
        dict_form = self.state.to_dict()
        self.assertIn('__class__', dict_form.keys())
        self.assertIn('State', dict_form.values())

    def test_compare_dict_object(self):
        dict_form = self.state.to_dict()
        self.assertEqual(self.state.id, dict_form['id'])
        self.assertTrue(
            self.state.created_at == datetime.fromisoformat(
                    dict_form['created_at']
                    )
            )

    def test_create_from_dict(self):
        self.state.name = "Holberton"
        state_copy = State(**self.state.to_dict())
        self.assertEqual(self.state.id, state_copy.id)
        self.assertEqual(self.state.created_at, state_copy.created_at)
        self.assertEqual(state_copy.name, "Holberton")
