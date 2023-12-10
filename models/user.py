#!/usr/bin/python3
"""The User class Module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    first_name = ""
    last_name = ""
    email = ""
    pasword = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new User instance."""
        super().__init__(*args, **kwargs)
