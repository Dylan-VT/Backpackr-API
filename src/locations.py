"""
Primary classes for backpackr locations. We will be uses pydantic models to make an api schema
Will define the following classes
Region: A class containing a grouping of countries for orginzational purposes
Country: A country with content available
Location: A place (i.e. a city or town) within a country to visit
Destination: A place to see or a thing to do. this will likely be used as a super class.
Think a business
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from helper_models import PyObjectId



class Country(BaseModel):
    """
    Highest level of region in backpackr
    """
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str = None


    class Config:
        """Config from https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
        """
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Location(BaseModel):
    """
    A location in a country. This would be something along the lines of a city
    """
    name: str = None
    country: Country = None


class Destination(BaseModel):
    """
    A thing to do, a place to see, or something to eat.
    """
    name: str = None
    location: Location = None



class Region(BaseModel):
    """
    A group of countries, the highest level region
    """
    name: str = None
    member_countries: List[Country] = []
