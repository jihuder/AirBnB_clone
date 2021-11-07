#!/usr/bin/python3
'''Module:  File base_model'''
import uuid
from datetime import datetime
import models


class BaseModel:
    ''' BaseModel:
        We design attributes and methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''Constructor of Base Model'''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at" "updated_at"]:
                    self.__dict__[key] = datetime.srtptime
                    (value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Prints the name, class and its dictionary'''
        msg = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
        return msg

    def save(self):
        ''' Update attribute with Datatime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' Creates a representation
              of the object from its __dict__ '''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        return dictionary
