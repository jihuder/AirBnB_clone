#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test cases for Amenity class """

    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_instance_BaseModel(self):
        """ Tests inheritance """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_instaciacion(self):
        """ Tests correct instatiation of the class """
        am = Amenity()
        am.name = "Charlie"
        self.assertIn("name", am.to_dict())

    def test_to_dict(self):
        """ Tests that the function retrieves a dictionary """
        base = Amenity()
        ret_dict = base.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test_str(self):
        """ Tests the str repr. of an object """
        base = Amenity()
        base_str = base.__str__()
        self.assertTrue(isinstance(base_str, str))

    def test_save(self):
        """ Tests the save method """
        base = Amenity()
        time1 = base.updated_at
        base.save()
        time2 = base.updated_at
        self.assertNotEqual(time1, time2)
