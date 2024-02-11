#!/usr/bin/python3
"""
file_storage manage storage
"""

import json
from models.base_model import BaseModel


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
        class_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''save objs to json file'''
        dictionary = {}
        for key in FileStorage.__objects:
            dictionary[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(dictionary))

    def reload(self):
        '''load objs from json file'''
        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionary = json.loads(file.read())
            for key in dictionary:
                self.new(eval(dictionary[key]["__class__"])(**dictionary[key]))
        except IOError:
            pass
