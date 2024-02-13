#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from airbnb_console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test suite for the HBNBCommand class."""

    def setUp(self):
        """Set up HBNBCommand instance."""
        self.cmd = HBNBCommand()

    def tearDown(self):
        """Clean up after each test."""
        self.cmd = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test help command."""
        with redirect_stdout(mock_stdout):
            self.cmd.onecmd('help')
        output = mock_stdout.getvalue()
        self.assertIn('Documented commands (type help <topic>):', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_classname(self, mock_stdout):
        """Test create command with missing classname."""
        with redirect_stdout(mock_stdout):
            self.cmd.onecmd('create')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '** class name missing **')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_classname(self, mock_stdout):
        """Test create command with invalid classname."""
        with redirect_stdout(mock_stdout):
            self.cmd.onecmd('create invalid_class')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '** class doesn\'t exist **')

    # Add more test cases for other commands as needed

if __name__ == '__main__':
    unittest.main()
