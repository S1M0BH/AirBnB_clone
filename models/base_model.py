#!/usr/bin/python3
"""BaseModel"""
from datetime import datetime
import models
import uuid



class BaseModel:
    """Base model class."""

    def __init__(self, *args, **kwargs):
        """Initialize the basic form."""
        timef = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(val, timef))
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of the base form"""
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def save(self):
        """updated_at updated with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the base form dictionary representation"""
        is_dict = self.__dict__.copy()
        is_dict['__class__'] = self.__class__.__name__
        is_dict['created_at'] = self.created_at.isoformat()
        is_dict['updated_at'] = self.updated_at.isoformat()
        return is_dict
