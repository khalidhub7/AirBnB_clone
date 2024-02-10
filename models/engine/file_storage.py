#!/usr/bin/python3
"""
file_storage that manages
our storage
"""

import json
from models.base_model import BaseModel


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
        """
        Add new object to objects dictionary
        """
        class_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''save objects to json file'''
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """ load objects from json file """
        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionary = json.loads(file.read())
            for key in dictionary:
                self.new(eval(dictionary[key]["__class__"])(**dictionary[key]))
        except IOError:
            pass
