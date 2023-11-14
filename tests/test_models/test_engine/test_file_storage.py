#!/usr/bin/python3
"""
Module for FilStorage unittest
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Testing methods of the FileStorage class.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        _base_model = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        _city = City()
        _amenity = Amenity()
        _review = Review()
        models.storage.new(_base_model)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        models.storage.new(_amenity)
        models.storage.new(_review)
        self.assertIn\(
                "BaseModel." + _base_model.id, models.storage.all().keys()
        )
        self.assertIn(_base_model, models.storage.all().values())
        self.assertIn("User." + _user.id, models.storage.all().keys())
        self.assertIn(_user, models.storage.all().values())
        self.assertIn("State." + _state.id, models.storage.all().keys())
        self.assertIn(_state, models.storage.all().values())
        self.assertIn("Place." + _place.id, models.storage.all().keys())
        self.assertIn(_place, models.storage.all().values())
        self.assertIn("City." + _city.id, models.storage.all().keys())
        self.assertIn(_city, models.storage.all().values())
        self.assertIn("Amenity." + _amenity.id, models.storage.all().keys())
        self.assertIn(_amenity, models.storage.all().values())
        self.assertIn("Review." + _review.id, models.storage.all().keys())
        self.assertIn(_review, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        _base_model = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        _city = City()
        _amenity = Amenity()
        _review = Review()
        models.storage.new(_base_model)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        models.storage.new(_amenity)
        models.storage.new(_review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + _base_model.id, save_text)
            self.assertIn("User." + _user.id, save_text)
            self.assertIn("State." + _state.id, save_text)
            self.assertIn("Place." + _place.id, save_text)
            self.assertIn("City." + _city.id, save_text)
            self.assertIn("Amenity." + _amenity.id, save_text)
            self.assertIn("Review." + _review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        _base_model = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        _city = City()
        _amenity = Amenity()
        _review = Review()
        models.storage.new(_base_model)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        models.storage.new(_amenity)
        models.storage.new(_review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + _base_model.id, objs)
        self.assertIn("User." + _user.id, objs)
        self.assertIn("State." + _state.id, objs)
        self.assertIn("Place." + _place.id, objs)
        self.assertIn("City." + _city.id, objs)
        self.assertIn("Amenity." + _amenity.id, objs)
        self.assertIn("Review." + _review.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
