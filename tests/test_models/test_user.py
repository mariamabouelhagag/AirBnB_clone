#!/usr/bin/python3
"""the User model uinte test"""

import unittest

from models.user import User


class Test_User_model(unittest.TestCase):
    """test class for the User model."""

    def test_default_value_instance(self):
        """test the default values for the User model"""
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
