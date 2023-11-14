#!/usr/bin/python3
"""
Base Model Class
defines all common attributes/methods
for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S,%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        method that updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
         method that returns a dictionary containing all keys/values
         of __dict__ of the instance
        """
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        return object_dict

    def __str__(self):
        """
        method that should print: [<class name>] (<self.id>) <self.__dict__>

        """
        className = self.__class__.__name__
        output = "[{}] ({}) {}".format(className, self.id, self.__dict__)
        return output
