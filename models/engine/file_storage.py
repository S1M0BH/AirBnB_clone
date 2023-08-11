#!/usr/bin/python3
"""storage category"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
import json
from models.review import Review


class FileStorage:
    """Format the volume"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Specifies the objects object with the key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializing objects to a JSON file"""
        odict = FileStorage.__objects
        data = {obj: odict[obj].to_dict() for obj in odict.keys()}

        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """JSON file deserializes objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
