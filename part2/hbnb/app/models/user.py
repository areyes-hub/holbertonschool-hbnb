from app.models.base import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if len(first_name) > 50:
            raise ValueError("first_name length must not exceed 50 characters")
        self.first_name = first_name
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if len(last_name) > 50:
            raise ValueError("last_name length must not exceed 50 characters")
        self.last_name = last_name
        if not isinstance(email, str):
            raise TypeError("email must be a string")
        if len(email) > 50:
            raise ValueError("email length must not exceed 50 characters")
        self.email = email
        self.is_admin = is_admin
        self.places = []


    def add_place(self, obj):
        self.places.append(obj)
