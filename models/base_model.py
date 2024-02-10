#!/usr/bin/python3
"""
base model parent of other classes
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Define
            BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the `BaseModel` object
        Args:
            *args: Additional args
            **kwargs: Additional keyword args

        Attributes:
            id: unique id
            created_at: datetime when an instance is created
            updated_at: datetime when an instance is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    pass
                elif key == "id":
                    self.id = kwargs[key]
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], "\
%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key], "\
%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        object descriptor
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict method that get an prepared dict
        Return:
            new dictionary
        """
        dictionary = {}
        for key in self.__dict__:
            dictionary[key] = self.__dict__[key]
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
