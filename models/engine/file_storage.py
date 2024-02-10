#!/usr/bin/python3
"""
file_storage that manages
our storage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    define a class
    FileStorage that manage objects storage
    attributes:
        __file_path (str): file storage path
        __objects (dict): dictionary of object created
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ get objects of the class """
        return FileStorage.__objects

    def new(self, obj):
        """ Add new object to objects dictionary """
        FileStorage.__objects["{}.{}\
".format(obj.to_dict()['__class__'], obj.id)] = obj

    def save(self):
        """ Save objects to json file """
        dictionary = {}
        for key in FileStorage.__objects:
            dictionary[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(dictionary))

    def reload(self):
        """ load objects from json file """
        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionary = json.loads(file.read())
            for key in dictionary:
                self.new(eval(dictionary[key]["__class__"])(**dictionary[key]))
        except IOError:
            pass
