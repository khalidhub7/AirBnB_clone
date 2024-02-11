#!/usr/bin/python3
"""basemodel unittest"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """basemodel unittest"""
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        """basemodel unittest"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """basemodel unittest"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """basemodel unittest"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """basemodel unittest"""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """basemodel unittest"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """basemodel unittest"""
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
