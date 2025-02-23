from app.models.base import BaseModel
from app.models.place import Place
from app.models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = str(text)
        self.rating = int(rating)
        if not isinstance(place, Place):
            raise ValueError("place must be an instance of Place")
        self.place = place
        if not isinstance(user, User):
            raise ValueError("user must be an instance of User")
        self.user = User(user)
