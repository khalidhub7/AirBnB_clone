#!/usr/bin/python3
'''comment 4 test'''

import datetime
import uuid
import models


class BaseModel:
    '''comment 4 test'''
    def __init__(self, *args, **kwargs):
        '''comment 4 test'''
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())

        if kwargs != None:
            formatt = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                if k == 'created_at':
                    self.__dict__[k] = datetime.datetime.strptime(v, formatt)
                if k == 'updated_at':
                    self.__dict__[k] = datetime.datetime.strptime(v, formatt)
                else:
                    self.__dict__[k] = v
        else:
            self.__dict__ = self.__dict__
            models.storage.new(self)

    def __str__(self):
        '''comment 4 test'''
        return "[{}] ({}) {}"\
        .format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        '''comment 4 test'''
        self.updated_at = datetime.datetime.now()
        models.storage.save()
    
    def to_dict(self):
        '''comment 4 test'''
        new__dict = self.__dict__.copy()
        new__dict['__class__'] = self.__class__.__name__
        new__dict['created_at'] = self.created_at.isoformat()
        new__dict['updated_at'] = self.updated_at.isoformat()
        new__dict['id'] = self.id
        return new__dict
