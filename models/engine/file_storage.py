#!/usr/bin/python3
"""Module containing FileStorage class
it serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
import os

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
        objs_dict = {}
        for obj in objs.keys():
            objs_dict[obj] = objs[obj].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(objs_dict, file)
    
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    objct_dict = json.loqd(file)
                    for key, value in objct_dict.items():
                        cls_name, objct_id = key.split('.')
                        _class = eval(cls_name)
                        instc = _class(**values)
                        FileStorage.__objects[key] = instc
                except Exception:
                    pass
