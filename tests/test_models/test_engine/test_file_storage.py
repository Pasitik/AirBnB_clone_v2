#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models import storage
import os
from sqlalchemy.orm import make_transient


class test_Storage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
        del_list = []
        for key in storage.all():
            del_list.append(key)

        for key in del_list:
            if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
                class_name = key.partition('.')[0]
                try:
                    storage.truncate_tables(classes[class_name], storage.all()[key].id)
                except:
                    pass
            else:
                del storage.all()[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            new = State(name='Accra')
        else:
            new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)
    

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            pass
        else:
            self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            new = State(name="Accra")
            new.save()
            self.assertNotEqual(len(storage.all()), 0)
        else:
            new = BaseModel()
            thing = new.to_dict()
            new.save()
            new2 = BaseModel(**thing)
            self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            new = State(name="Accra")
            new.save()
            self.assertNotEqual(len(storage.all()), 0)
        else:
            """ FileStorage save method """
            new = BaseModel()
            storage.save()
            self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            pass
        else:
            new = BaseModel()
            new.save()
            storage.save()
            storage.reload()
            for obj in storage.all().values():
                loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            storage.reload()
        else:
            with open('file.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            new = State(name="Accra")
            new.save()
            self.assertTrue(len(storage.all()) > 0)
        else:
            new = BaseModel()
            new.save()
            self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            pass
        else:
            self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            new = State(name="Accra")
            new.save()
            _id = new.to_dict()['id']
            for key in storage.all().keys():
                temp = key
            self.assertEqual(temp, 'State' + '.' + _id)
        else:
            new =  BaseModel()
            new.save()
            _id = new.to_dict()['id']
            for key in storage.all().keys():
                temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        from models.engine.db_storage import DBStorage
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            self.assertEqual(type(storage), DBStorage)
        else:
            self.assertEqual(type(storage), FileStorage)

    def test_storage_var_deleted(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        from models.state import State

        pass
        if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
            fs = storage
        else:
            fs = FileStorage()

        new_state = State(name="California")
        storage.new(new_state)
       
        fs.save()


        another_state = State(name="nevada")
        fs.new(another_state)
        fs.save()

        fs.delete(new_state)
        all_states = fs.all(State)

        self.assertTrue(len(all_states), 1)
