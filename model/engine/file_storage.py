#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """Delete obj from __objects if it exists"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        filtered_objects = {}
        for key, value in FileStorage.__objects.items():
            if cls == value.__class__:
                filtered_objects[key] = value
        return filtered_objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the storage dictionary to a file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads the storage dictionary from a file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    if class_name in classes:
                        self.new(classes[class_name](**val))
        except FileNotFoundError:
            pass

    def close(self):
        """
        Calls the reload() method to deserialize
        the JSON file to objects.
        """
        self.reload()
