#!/usr/bin/python3
"""The Review class Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review Class"""
    user_id = ""
    place_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
