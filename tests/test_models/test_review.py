#!/usr/bin/python3
"""
This module defines a unittest class for Review class
of the file review.py of models module
"""
import unittest
from models.review import Review
from datetime import datetime
import uuid


class TestReview(unittest.TestCase):
    """This is the unittest class for 'Review' class."""

    def setUp(self):
        self.review = Review()

    def test_date_type(self):
        self.assertTrue(isinstance(self.review.created_at, datetime))
        self.assertTrue(isinstance(self.review.updated_at, datetime))
        self.assertFalse(isinstance(self.review.created_at, str))

    def test_uuid(self):
        with self.assertRaises(ValueError):
            uuid_obj = uuid.UUID(self.review.id, version=4)
            if uuid_obj:
                raise ValueError

    def test_dates(self):
        self.assertFalse(self.review.created_at > datetime.now())
        self.assertFalse(self.review.updated_at < self.review.created_at)

    def test_to_dict(self):
        dict_form = self.review.to_dict()
        self.assertIn('__class__', dict_form.keys())
        self.assertIn('Review', dict_form.values())

    def test_compare_dict_object(self):
        dict_form = self.review.to_dict()
        self.assertEqual(self.review.id, dict_form['id'])
        self.assertTrue(
            self.review.created_at == datetime.fromisoformat(
                    dict_form['created_at']
                    )
            )

    def test_create_from_dict(self):
        self.review.name = "Holberton"
        review_copy = Review(**self.review.to_dict())
        self.assertEqual(self.review.id, review_copy.id)
        self.assertEqual(self.review.created_at, review_copy.created_at)
        self.assertEqual(review_copy.name, "Holberton")
