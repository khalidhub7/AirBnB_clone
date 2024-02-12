#!/usr/bin/python3
"""
file_storage manage storage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """
    define a class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        return class objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add new obj to objects dictionary
        """
        keyy = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[keyy] = obj

    def save(self):
        """
        Save objects to json__file
        """
        to__json = {}
        for i in FileStorage.__objects:
            to__json[i] = FileStorage.__objects[i].to_dict()
            '''drna call l to_dict() method to convert it to a dictionary'''
        with open(FileStorage.__file_path, "w", encoding='UTF-8') as myfile:
            myfile.write(json.dumps(to__json))

    def reload(self):
        """
        load objects from json__file
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as myfile:
                mydata = json.load(myfile)
                for key, value in mydata.items():
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
