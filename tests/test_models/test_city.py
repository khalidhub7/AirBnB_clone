#!/usr/bin/python3
"""test city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """test city"""
    def setUp(self):
        """test city"""
        self.city = City()

    def test_inheritance(self):
        """test city"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes_initialization(self):
        """test city"""
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')


if __name__ == '__main__':
    unittest.main()
