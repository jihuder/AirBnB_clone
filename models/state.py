#!/usr/bin/python3
"""Module: state.py"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class
        Public class attributes:
            name: string - empty string"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Class constructor for State"""
        super().__init__(*args, **kwargs)
