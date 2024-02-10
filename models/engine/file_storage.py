#!/usr/bin/python3
"""
file_storage that manages storage
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    define a classFileStorage

    __file_path: file storage
    __objects: dictionary of object created
    """
    __file_path = 'file.json'
    __objects = {}
    storage = 0

    def all(self):
        """
        get objects of the class
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add new object to objects dictionary
        """
        key = "{}.id".format(obj.__class__.__name__) # ymkn ndir assign l id b self.id
        self.__objects[key] = obj

    def save(self):
        """
        save objects to json file
        """
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        load objects from json file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
