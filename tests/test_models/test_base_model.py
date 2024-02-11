#!/usr/bin/python3
'''test BaseModel'''
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''test BaseModel'''
    def setUp(self):
        '''test BaseModel'''
        self.base_model = BaseModel()

    def test_id_is_string(self):
        '''test BaseModel'''
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        '''test BaseModel'''
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        '''test BaseModel'''
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        '''test BaseModel'''
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        '''test BaseModel'''
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        '''test BaseModel'''
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
