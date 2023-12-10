#!/usr/bin/python3
"""the State class module"""

from models.base_model import BaseModel


class State(BaseModel):
    """the State Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new State instance."""
        super().__init__(*args, **kwargs)
