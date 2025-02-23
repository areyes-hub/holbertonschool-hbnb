from base import BaseModel
from user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        if not isinstance(owner, User):
            raise ValueError("owner must be an instance of User")
        self.owner = owner
        self.reviews = []
        self.amenities = []


    def add_reviews(self, review):
        self.reviews.append(review)


    def add_amenities(self, amenity):
        self.amenities.append(amenity)
