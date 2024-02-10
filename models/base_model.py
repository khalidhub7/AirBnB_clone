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
        """ if kwargs:
            for i in kwargs:
                if i == "__class__":
                    pass
                elif i == "id":
                    self.id = kwargs[i]
                elif i == "created_at":
                    self.created_at = kwargs[i]
                elif i == "updated_at":
                    self.updated_at = kwargs[i]
                else:
                    setattr(self, i, kwargs[i]) """
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
            self.id = str(uuid4())
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
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = datetime.now().isoformat()
        mydict['updated_at'] = datetime.now().isoformat()
        return mydict
