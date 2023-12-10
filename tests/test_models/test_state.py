#!/usr/bin/python3
"""the State model unite test"""

import unittest

from models.state import State


class Test_State_model(unittest.TestCase):
    """State modeltest class."""

    def test_default_values(self):
        """test a default values for the state model"""
        state = State()
        self.assertEqual(state.name, "")
