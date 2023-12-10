#!/usr/bin/python3
"""Define the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity instance."""
        super().__init__(*args, **kwargs)
