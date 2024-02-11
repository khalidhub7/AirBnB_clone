#!/usr/bin/python3
"""FileStorage tests"""
import unittest
import os
import json
from unittest.mock import patch, mock_open
from models.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """FileStorage tests"""
    def setUp(self):
        self.file_path = "file.json"
        self.file_storage = FileStorage()

    def tearDown(self):
        """FileStorage tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method_empty(self):
        """FileStorage tests"""
        self.assertEqual(self.file_storage.all(), {})

    def test_new_method(self):
        """FileStorage tests"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.file_storage.all())

    def test_save_method(self):
        """FileStorage tests"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()

        with open(self.file_path, "r") as file:
            data = json.load(file)
            self.assertIn(f"BaseModel.{obj.id}", data)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_method_with_mock(self, mock_open_func):
        """FileStorage tests"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        mock_open_func.assert_called_once_with(self.file_path, "w")
        mock_open_func().write.assert_called_once()

    def test_reload_method(self):
        """FileStorage tests"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.file_storage.all())

    @patch("builtins.open", new_callable=mock_open, read_data='{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234"}}')
    def test_reload_method_with_mock(self, mock_open_func):
        """FileStorage tests"""
        self.file_storage.reload()
        mock_open_func.assert_called_once_with(self.file_path, "r")
        self.assertIn("BaseModel.1234", self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
