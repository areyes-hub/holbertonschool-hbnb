from app.models.base import BaseModel
from app.models.place import Place
from app.models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.text = text
        if not isinstance(rating, int):
            raise TypeError("rating must be an integer")
        if 1 > rating > 5:
            raise ValueError("rating must be between 1 - 5")
        self.rating = rating
        if not isinstance(place, Place):
            raise ValueError("place must be an instance of Place")
        self.place = place
        if not isinstance(user, User):
            raise ValueError("user must be an instance of User")
        self.user = User(user)
