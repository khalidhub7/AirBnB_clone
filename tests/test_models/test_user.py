#!/usr/bin/python3
"""test user"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test user"""
    def setUp(self):
        """test user"""
        self.user = User()

    def test_inheritance(self):
        """test user"""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes_initialization(self):
        """test user"""
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')


if __name__ == '__main__':
    unittest.main()
