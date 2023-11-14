#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class to handle informations
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
