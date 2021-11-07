#!/usr/bin/python3
"""
    This module contains test cases for amenity.py
"""
import unittest
import json
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """" Unitest cases for File_Storage class """
    def setUp(self) -> None:
        super().setUp()
        self.obj_0 = BaseModel()
        self.obj_1 = User()
        self.obj_2 = State()
        self.obj_3 = City()
        self.obj_4 = Amenity()
        self.obj_5 = Place()
        self.obj_6 = Review()
        self.objs = [
                        self.obj_0, self.obj_1, self.obj_2,
                        self.obj_3, self.obj_4, self.obj_5, self.obj_6]
        self.all_objs = models.storage.all()
        self.all_objs = {}

    def test_empty_file(self):
        # all obj
        all_obj = models.storage.all()
        print(all_obj)
        # reload doens´t return error
        self.assertEqual(models.storage.reload(), None)

    def test_create_save_reload_objs(self):
        # add objs with new method
        for obj in self.objs:
            models.storage.new(obj)
        # all obj
        all_obj_0 = models.storage.all()
        '#Save'
        models.storage.save()
        # reload
        models.storage.reload()
        # same objs
        all_obj_1 = models.storage.all()
        self.assertEqual(all_obj_0, all_obj_1)
