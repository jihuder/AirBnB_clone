#!/usr/bin/python3
"""Module: amenity.py"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class
        Public class attributes:
            name: string - empty string"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Class constructor for Amenity"""
        super().__init__(*args, **kwargs)
