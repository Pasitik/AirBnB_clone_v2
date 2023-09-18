#!/usr/bin/python3
"""A unit test to test the console"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from tests import clear_stream
from models import storage
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """test class for the HBNBCommand class."""
    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_create(self):
        """test create in console"""
        with patch('sys.stdout', new=StringIO()) as print_out:
            console = HBNBCommand()
            console.onecmd('create City name="Texas"')
            mid = print_out.getvalue().strip()
            clear_stream(print_out)
            self.assertIn('City.{}'.format(mid), storage.all().keys())
            console.onecmd('show City {}'.format(mid))
            self.assertIn("'name': 'Texas'", print_out.getvalue().strip())
            clear_stream(print_out)
            console.oncmd('create User name="James" age=17 height=5.9')
            mid = print_out.getvalue().strip()
            self.assertIn('User.{}'.format(mid), storage.all().keys())
            clear_stream(print_out)
            console.onecmd('show User {}'.format(mid))
            self.assertIn("'name': 'James'", print_out.getvalue().strip())
            self.assertIn("'age': 17", print_out.getvalue().strip())
            self.assertIn("'height': 5.9", print_out.getvalue().strip())
