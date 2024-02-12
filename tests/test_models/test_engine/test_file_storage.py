#!/usr/bin/python3

"""Tests for FileStorage class."""

import unittest
from unittest.mock import mock_open, patch
import json
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = "file.json"
        self.file_storage = FileStorage()

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method_empty(self):
        """Test all method with empty file."""
        self.assertEqual(self.file_storage.all(), {})

    def test_new_method(self):
        """Test new method."""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.file_storage.all())

    @patch("builtins.open", new_callable=mock_open)
    def test_save_method(self, mock_open_func):
        """Test save method."""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        mock_open_func.assert_called_once_with(self.file_path, "w")
        mock_open_func().write.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data='{"BaseModel.1234": {"__class__": "BaseModel", "id": "1234"}}')
    def test_reload_method(self, mock_open_func):
        """Test reload method."""
        self.file_storage.reload()
        mock_open_func.assert_called_once_with(self.file_path, "r")
        self.assertIn("BaseModel.1234", self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
