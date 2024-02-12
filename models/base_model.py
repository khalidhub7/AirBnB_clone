#!/usr/bin/python3
'''BaseModel parent of other classes'''

import datetime
import uuid
import models


class BaseModel:
    '''BaseModel class'''
    def __init__(self, *args, **kwargs):
        '''BaseModel initialization'''
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())

        if kwargs:
            formatt = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                if k == 'created_at':
                    self.__dict__[k] = datetime.datetime.strptime(v, formatt)
                elif k == 'updated_at':
                    self.__dict__[k] = datetime.datetime.strptime(v, formatt)
                else:
                    self.__dict__[k] = v
        else:
            self.__dict__ = self.__dict__
            models.storage.new(self)

    def __str__(self):
        '''str representation'''
        return "[{}] ({}) {}"\
        .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''updated_at instance attribute'''
        self.updated_at = datetime.datetime.now()
        models.storage.save(self)

    def to_dict(self):
        '''to_dict method'''
        new__dict = self.__dict__.copy()
        new__dict['__class__'] = self.__class__.__name__
        new__dict['created_at'] = self.created_at.isoformat()
        new__dict['updated_at'] = self.updated_at.isoformat()
        new__dict['id'] = self.id
        return new__dict
