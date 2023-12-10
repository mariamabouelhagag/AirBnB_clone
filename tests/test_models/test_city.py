#!/usr/bin/python3
"""Unittest for the City model"""

import unittest

from models.city import City


class Test_City_model(unittest.TestCase):
    """Unittest for testing the city modle."""

    def test_default_values(self):
        """Unittest for testing the default value for the city model"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
