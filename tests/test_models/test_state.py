#!/usr/bin/python3
'''test state'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''test state'''
    def setUp(self):
        '''test state'''
        self.state = State()

    def test_inheritance(self):
        '''test state'''
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes_initialization(self):
        '''test state'''
        self.assertEqual(self.state.name, '')


if __name__ == '__main__':
    unittest.main()
