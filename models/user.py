#!/usr/bin/python3
"""user category"""
from models.base_model import BaseModel

class User(BaseModel):
    """Initialize the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
