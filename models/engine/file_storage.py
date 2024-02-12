#!/usr/bin/python3

"""
File storage for managing storage.
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
    '''
    Define a class for file storage.

    Attributes:
        __file_path (str): Path to the storage file.
        __objects (dict): Dictionary of created objects.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Get all objects of a class.'''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Add a new object to the objects dictionary.

        Args:
            obj: Object to be added.
        '''
        class_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''Save objects to a JSON file.'''
        dictionary = {}
        for key in FileStorage.__objects:
            dictionary[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(dictionary))

    def reload(self):
        '''Load objects from a JSON file.'''
        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionary = json.loads(file.read())
            for key in dictionary:
                self.new(eval(dictionary[key]["__class__"])(**dictionary[key]))
        except IOError:
            pass
