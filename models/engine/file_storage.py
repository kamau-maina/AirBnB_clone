#!/usr/bin/python3
"""
In this module we recreate BaseModel by using
dictionary representation
"""

import json
import uuid
import os
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """ serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the dictionary in __object with obj
        with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serializes objs to JSON file (path:__file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as filename:
            new_dict  {key: obj.to_dict() for key, obj in
                       FileStorage.__objects.items()}
            json.dump(new_dict, filename)

    def reload(self):
        """Reload the file"""
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding='utf-8')
            as filename:
                load_json = json.load(filename)
                for key, value in load_json.items():
                    FileStorage.__objects[key] = eval(
                            value['__class__'])(**value)
