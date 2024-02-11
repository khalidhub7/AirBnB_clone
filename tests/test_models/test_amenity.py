#!/usr/bin/python3
"""test amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test amenity"""
    def setUp(self):
        """test amenity"""
        self.amenity = Amenity()

    def test_inheritance(self):
        """test amenity"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes_initialization(self):
        """test amenity"""
        self.assertEqual(self.amenity.name, '')


if __name__ == '__main__':
    unittest.main()
