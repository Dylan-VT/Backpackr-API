"""
Currently contains helper models and classes that don't fit in another file
"""
from bson import ObjectId

class PyObjectId(ObjectId):
    """
    Handles ObjectIDs from Mongoose. Found on:
    https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, val):
        """
        Check if valid object id
        """
        if not ObjectId.is_valid(val):
            raise ValueError("Invalid objectid")
        return ObjectId(val)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
