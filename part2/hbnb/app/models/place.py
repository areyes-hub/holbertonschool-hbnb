from app.models.base import BaseModel
from app.models.user import User
from app.models.amenity import Amenity


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) > 100:
            raise ValueError("title length must not exceed 50 characters")
        self.title = title
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self.description = description
        if not isinstance(price, float):
            raise TypeError("price must be a float")
        self.price = price
        if not isinstance(latitude, float):
            raise TypeError("latitude must be a float")
        if latitude < -90.0 and latitude > 90.0:
            raise ValueError("latitude is out of range")
        self.latitude = latitude
        if not isinstance(longitude, float):
            raise TypeError("longitude must be a float")
        if longitude < -180.0 and longitude > 180.0:
            raise ValueError("longitude is out of range")
        self.longitude = longitude
        if not isinstance(owner, User):
            raise ValueError("owner must be an instance of User")
        self.owner = owner
        self.reviews = []
        self.amenities = []


    def add_review(self, review):
        self.reviews.append(review)


    def add_amenities(self, amenity):
        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be an instance of Amenity")
        self.amenities.append(amenity)
