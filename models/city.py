#!/usr/bin/python3
"""Define the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance."""
        super().__init__(*args, **kwargs)
