#!/usr/bin/python3
"""
Defines all common attributes/method for other classes
"""


import uuid
from datetime import datetime


class BaseModel:
    """Class constructor"""

    def __init__(self):
        """Define public instance attributes"""

        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def __str__(self):
        """prints string representation"""

        return f"[{type(self).__name__}], ({self.id}), {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with
            the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
            of__dict__ of the instance
        """

        self.updated_at = self.updated_at.isoformat()
        self.created_at = self.created_at.isoformat()

        return self.__dict__
