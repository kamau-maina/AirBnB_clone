#!/usr/bin/python3
"""
In this module we recreate BaseModel by using
dictionary representation
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
#!/usr/bin/python3
"""
This module contains a class FileStorage that serializes
instances to a JSON file and deserializes JSON file to
instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
import os.path


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def all(self):
        """returns the dictionary `objects` """
        return FileStorage.__objects

    def new(self, obj):
        """sets obj.id as key in dictionary(objects)"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes the dictionary(objects) to the JSON file"""

        """
        make a copy of __objects to enable the values to be
        changed to a dictionary representation. This ensures
        __objects always stores data in a uniform format as
        {key : obj} and not {key : obj.to_dict()}
        """
        my_dict = {}

        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(my_dict, json_file)

    def reload(self):
        """deserializes JSON file to objects(dictionary)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                FileStorage.__objects = json.load(json_file)
            for key, val in FileStorage.__objects.items():
                FileStorage.__objects[key] = FileStorage.class_dict[val["__class__"]](**val)



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
            new_dict = {key: obj.to_dict() for key, obj in
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
