#!/usr/bin/python3
""" This city module
give the name of the city
"""


from models.base_model import BaseModel


class City(BaseModel):
    """This class gives state -id and  name of the city"""
    state_id = ""
    name = ""
