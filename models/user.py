#!/usr/bin/python3
"""the user module
shows the user infor
"""


from models.base_model import BaseModel


class User(BaseModel):
    """class user shows the name, email
    passwordof the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
