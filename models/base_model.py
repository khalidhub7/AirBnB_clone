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
        initialize BaseModel obj
        *args: args if exist
        **kwargs: keyword args if exist

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
            models.storage.new(self)

    def __str__(self):
        """
        obj descriptor
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        update the updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        get a prepared dict
        '''
        my_dict = {}
        for key in self.__dict__:
            my_dict[key] = self.__dict__[key]
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
