#!/usr/bin/python3
"""
    Model: file_storage
    dictionary representation to a JSON string
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return(FileStorage.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_dict = {}
        with open(FileStorage.__file_path, "w") as path:
            for key, obj in FileStorage.__objects.items():
                json_dict[key] = obj.to_dict()
            my_string = json.dumps(json_dict)
            path.write(my_string)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as path:
                my_dict = json.load(path)
                classes = ["BaseModel", "User", "State",
                           "City", "Amenity", "Place", "Review"]
                for key, value in my_dict.items():
                    _class = key.split('.')[0]
                    if _class in classes:
                        my_obj = eval(_class+"(**value)")
                        self.new(my_obj)
        except:
            pass
