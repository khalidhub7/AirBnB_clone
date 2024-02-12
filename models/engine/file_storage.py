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
    '''
    define a class
    __file_path: storage path
    __objects: dict of obj created
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''get objs of class'''
        return FileStorage.__objects

    def new(self, obj):
        '''
        add new obj to objs dict
        '''
        keyy = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[keyy] = obj

    def save(self):
        '''save objs to json file'''
        to__json = {}
        for i in FileStorage.__objects:
            to__json[i] = FileStorage.__objects[i].to_dict()
            '''drna call l to_dict() method to convert it to a dictionary'''
        with open(FileStorage.__file_path, "w", encoding='UTF-8') as myfile:
            myfile.write(json.dumps(to__json))

    def reload(self):
        '''load objs from json file'''
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
