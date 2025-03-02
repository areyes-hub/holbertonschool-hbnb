import unittest
from app import create_app
import uuid


class TestUserEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()


    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jean",
            "last_name": "Doe",
            "email": "jean.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)


    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "Invalid-email"
        })
        self.assertEqual(response.status_code, 400)


    def test_get_all_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)


class TestPlaceEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Janet",
            "last_name": "Smith",
            "email": "janet.smith@example.com"
        })
        user = user_response.get_json()
        if 'id' in user:
            self.user_id = user['id']
        else:
            print(f"User creation failed: {user}")
            self.user_id = None
        response = self.client.post('/api/v1/places/', json={
            "title": "Beachfront Villa",
            "description": "A beautiful beachfront property",
            "price": 200.50,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "owner": {"id": self.user_id}
        })
        self.assertEqual(response.status_code, 201)
        place = response.get_json()
        self.assertIn('id', place)
        self.place_id = place['id']


    def test_create_place(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "Beachfront Villa",
            "description": "A beautiful beachfront property",
            "price": 200.50,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "owner": {"id": self.user_id}
        })
        self.assertEqual(response.status_code, 201)


    def test_get_place_by_id(self):
        response = self.client.get(f'/api/v1/places/{self.place_id}')
        self.assertEqual(response.status_code, 200)


    def test_get_all_places(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)


class TestAmenityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Swimming Pool"
        })
        amenity = response.get_json()
        self.assertIn('id', amenity)
        self.amenity_id = amenity["id"]


    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Swimming Pool"
        })
        self.assertEqual(response.status_code, 201)


    def test_get_amenity_by_id(self):
        response = self.client.get(f'/api/v1/amenities/{self.amenity_id}')
        self.assertEqual(response.status_code, 200)


    def test_get_all_amenities(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)


    def test_update_amenity(self):
        response = self.client.put(f'/api/v1/amenities/{self.amenity_id}', json={
            "name": "WI-FI"
        })
        self.assertEqual(response.status_code, 200)


class TestReviewEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Janis",
            "last_name": "Smith",
            "email": "janis.smith@example.com"
        })
        user = user_response.get_json()
        if 'id' in user:
            self.user_id = user['id']
        else:
            print(f"User creation failed: {user}")
            self.user_id = None
        response = self.client.post('/api/v1/places/', json={
            "title": "Beachfront Villa",
            "description": "A beautiful beachfront property",
            "price": 200.50,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "owner": {"id": self.user_id}
        })
        self.assertEqual(response.status_code, 201)
        place = response.get_json()
        self.assertIn('id', place)
        self.place_id = place['id']
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Amazing place!",
            "rating": 5,
            "user_id": self.user_id,
            "place_id": self.place_id
        })
        self.assertEqual(response.status_code, 201)
        review = response.get_json()
        self.assertIn('id', review)
        self.review_id = review['id']


    def test_create_review(self):
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Fantastic stay!",
            "rating": 4,
            "user_id": self.user_id,
            "place_id": self.place_id
        })
        self.assertEqual(response.status_code, 201)


    def test_get_review_by_id(self):
        response = self.client.get(f'/api/v1/reviews/{self.review_id}')
        self.assertEqual(response.status_code, 200)


    def test_update_review(self):
        response = self.client.put(f'/api/v1/reviews/{self.review_id}', json={
            "text": "Wonderful stay!",
            "rating": 5
        })
        self.assertEqual(response.status_code, 200)


    def test_get_review_by_place_id(self):
        response = self.client.get(f'/api/v1/places/{self.place_id}/reviews')
        self.assertEqual(response.status_code, 200)


    def test_delete_review(self):
        response = self.client.delete(f'/api/v1/reviews/{self.review_id}')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
