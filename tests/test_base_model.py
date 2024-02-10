#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel   # Importing your BaseModel class from your module

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_str(self):
        expected_output = f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_output)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict(self):
        expected_dict = {
            '__class__': self.base_model.__class__.__name__,
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
