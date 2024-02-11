#!/usr/bin/python3
'''file_storage tests'''
import unittest
from unittest.mock import mock_open, patch
import json
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''file_storage tests'''
    def setUp(self):
        '''file_storage tests'''
        self.file_path = "file.json"
        self.file_storage = FileStorage()

    def tearDown(self):
        '''file_storage tests'''
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method_empty(self):
        '''file_storage tests'''
        self.assertEqual(self.file_storage.all(), {})

    def test_new_method(self):
        '''file_storage tests'''
        obj = BaseModel()
        self.file_storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.file_storage.all())

    @patch("builtins.open", new_callable=mock_open)
    def test_save_method(self, mock_open_func):
        '''file_storage tests'''
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        mock_open_func.assert_called_once_with(self.file_path, "w")
        mock_open_func().write.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=\
            '{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234"}}')
    def test_reload_method(self, mock_open_func):
        '''file_storage tests'''
        self.file_storage.reload()
        mock_open_func.assert_called_once_with(self.file_path, "r")
        self.assertIn("BaseModel.1234", self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
