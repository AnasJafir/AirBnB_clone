#!/usr/bin/python3
"""Module containing FileStorage class
it serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class that serializes and deserializes datas
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        objct_name = obj.__class__.__name__
        key = "{}.{}".format(objct_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objs = FileStorage.__objects
        obj_dict = {}
        for obj in objs.keys():
            obj_dict[obj] = objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        cls_name, obj_id = key.split('.')
                        _class = eval(cls_name)
                        instc = _class(**value)
                        FileStorage.__objects[key] = instc
                except Exception:
                    pass
