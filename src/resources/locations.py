"""
Primary classes for backpackr locations. We will be uses pydantic models to make an api schema
Will define the following classes
Region: A class containing a grouping of countries for orginzational purposes
Country: A country with content available
Location: A place (i.e. a city or town) within a country to visit
Destination: A place to see or a thing to do. this will likely be used as a super class. Think a business
"""

from typing import List
from pydantic import BaseModel
class Attraction(BaseModel):
    """
    A thing to do, a place to see, or something to eat.
    """
    name: str


class Country(BaseModel):
    """
    Highest level of region in backpackr
    """
    name: str

class Region(BaseModel):
    """
    A group of countries, the highest level region
    """
    name: str
    member_countries = List[Country]

