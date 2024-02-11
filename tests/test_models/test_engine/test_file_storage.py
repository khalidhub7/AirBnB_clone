#!/usr/bin/python3
'''unittest for file_storage.py'''
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    '''unittest for file_storage.py'''
    def setUp(self):
        '''unittest for file_storage.py'''
        self.storage = storage
        self.base_model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def tearDown(self):
        '''unittest for file_storage.py'''
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all_method(self):
        '''unittest for file_storage.py'''
        self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        '''unittest for file_storage.py'''
        self.storage.new(self.base_model)
        self.assertIn('BaseModel.' + self.base_model.id, self.storage.all())

    def test_save_method(self):
        '''unittest for file_storage.py'''
        self.storage.new(self.base_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertTrue(len(content) > 0)

    def test_reload_method(self):
        '''unittest for file_storage.py'''
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        self.assertIn('BaseModel.' + self.base_model.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()
