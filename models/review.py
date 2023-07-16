#!/usr/bin/python3
"""The review module
shows the reviews of the place"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ this class shows the review of the place
    it will show the user.id, place.id and review
    """
    place_id = ""
    user_id = ""
    text = ""
