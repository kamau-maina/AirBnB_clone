#!/usr/bin/python3
"""This is the users module
it gives basic information about the user
"""


from models.base_model import BaseModel


class User(BaseModel):
    """The User class inherits from BaseModel
     Attr:
     email - str email
     password-
     first_name -
     last_name -
     """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
