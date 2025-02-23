from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    # Placeholder method for user creation
    def create_user(self, user_data):
        #logic will be implemented in later tasks
        pass


    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        #logic will be implemented in later tasks
        pass


    # Placeholder method for deleting a user
    def delete_user(self, user_data):
        pass
