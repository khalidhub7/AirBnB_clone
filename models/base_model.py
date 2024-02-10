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

    def __init__(self):
        """
        Initialize the `BaseModel` object

        Attributes:
            id: unique id
            created_at: datetime when an instance is created
            updated_at: datetime when an instance is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = datetime.now().isoformat()
        mydict['updated_at'] = datetime.now().isoformat()
        return mydict
