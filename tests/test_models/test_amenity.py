#!/usr/bin/python3
"""Unittest for the Amenity model"""

import unittest

from models.amenity import Amenity


class Test_Amenity_model(unittest.TestCase):
    """Unittest for testing the Amenity model."""

    def test_default_values(self):
        """Unittest for testing the default values for the Amenity model"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
