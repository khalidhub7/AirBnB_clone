#!/usr/bin/python3
'''test review'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''test review'''
    def setUp(self):
        '''test review'''
        self.review = Review()

    def test_inheritance(self):
        '''test review'''
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes_initialization(self):
        '''test review'''
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')


if __name__ == '__main__':
    unittest.main()
