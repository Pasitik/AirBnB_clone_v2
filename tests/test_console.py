import uuid
import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch, Mock
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import console
import time

class TestConsole(unittest.TestCase):
    #city_id, user_id, 
    state_id = ""

    def test_module_doc(self):
        """Test for module documentation"""
        self.assertIsNotNone(console.__doc__)

    def test_class_doc(self):
        """Test for class documentation"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_method_docs(self):
        """Test all methods in ``console`` for docs"""
        methods = [
            HBNBCommand.do_EOF,
            HBNBCommand.help_EOF,
            HBNBCommand.do_quit,
            HBNBCommand.help_quit,
            HBNBCommand.emptyline,
            HBNBCommand.do_create,
            HBNBCommand.help_create,
            HBNBCommand.do_show,
            HBNBCommand.help_show,
            HBNBCommand.do_destroy,
            HBNBCommand.help_destroy,
            HBNBCommand.do_all,
            HBNBCommand.help_all,
            HBNBCommand.do_update,
            HBNBCommand.default,
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_quit(self):
        """Test quit method"""
        pass

    def test_empty_line(self):
        """Test empty_line method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_create(self):
        """Test help_create method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_show(self):
        """Test help_show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_destroy(self):
        """Test help_destroy method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_all(self):
        """Test help_all method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_update(self):
        """Test help_update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)


    def test_create_with_valid_class_name_User(self):
        """Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'create User email="user@gmail"'
                ' password="passwordr@gmail" first'
                '_name="first_name@gmail"'
            )
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")
    
    @unittest.skip("demonstrating skipping")
    def test_create_with_valid_class_name_Place(self):
        """ Test create with valid class name"""
        city_id = ""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"Accra\"")
            state_id = f.getvalue().strip()
            HBNBCommand().onecmd("create City name=\"Accra\"")
            city_id = f.getvalue().strip()
            HBNBCommand().onecmd("create User name=\"John\"")
            user_id = f.getvalue().strip()
            HBNBCommand().onecmd(
                    f"create Place"
                    " name=\"My_little_house\" number_rooms=4"
                    " number_bathrooms=2 max_guest=10"
                    " price_by_night=300 latitude=37.773972"
                    " longitude=-122.431297 user_id=\"0001\""
                    )
            output = f.getvalue().strip()
            try:
             #print(f"output is {output}", file=sys.stderr)
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_State(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"Accra\"")
            self.state_id = f.getvalue().strip()
            try:
                uuid.UUID(self.state_id)
            except ValueError:
                self.fail("Output is not a valid UUID")

    @unittest.skip("demonstrating skipping")
    def test_create_with_valid_class_name_City(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as fa:
            HBNBCommand().onecmd("create State name=\"Accra\"")
            state_id = fa.getvalue().strip()
            time.sleep(5)
            if state_id is not None:
            # Create a City with the correct state_id
                HBNBCommand().onecmd("create City name=\"Tema\" state_id={}".format('\"'+ state_id +'\"'))
                #output = fa.getvalue().strip()
                try:
                    uuid.UUID(state_id)
                except ValueError:
                    self.fail("Output is not a valid UUID")

            # Ensure that the 'state_id' is set correctly in the City object
           # city = storage.get("City", output)
            #self.assertEqual(city.state_id, state_id)

    def test_create_with_valid_class_name_Amenity(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity name=\"wifi\"")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    @unittest.skip("demonstrating skipping")
    def test_create_with_valid_class_name_Review(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review name=\"myreview\"")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_without_class_name(self):
        """Test create without class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")
#
    def test_create_with_invalid_class_name(self):
        """Test create with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


if __name__ == "__main__":
    unittest.main()
