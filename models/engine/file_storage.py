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
        """ Save objects to json file """
        dictionary = {}
        for key in FileStorage.__objects:
            dictionary[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(dictionary))

    def reload(self):
        """
        load objects from json file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
