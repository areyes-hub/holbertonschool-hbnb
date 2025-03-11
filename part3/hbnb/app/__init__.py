from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.admin import api as admin_ns
from app.api.v1.auth import ProtectedResource
from app.api.v1.reviews import PlaceReviewsList
from app.api.v1.admin import AdminUserCreate, AdminUserModify
from app.api.v1.admin import AdminAmenityCreate, AdminAmenityModify
from app.api.v1.admin import AdminPlaceModify, AdminReviewModify

bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
    bcrypt.init_app(app)
    jwt.init_app(app)
    api = Api(app)

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(admin_ns, path='/api/v1/admin')

    api.add_resource(PlaceReviewsList, '/api/v1/places/<place_id>/reviews')
    api.add_resource(ProtectedResource, '/api/v1/protected')
    api.add_resource(AdminUserCreate, '/api/v1/users/')
    api.add_resource(AdminUserModify, '/api/v1/users/<user_id>')
    api.add_resource(AdminAmenityCreate, '/api/v1/amenities/')
    api.add_resource(AdminAmenityModify, '/api/v1/amenities/<amenity_id>')
    api.add_resource(AdminPlaceModify, '/api/v1/places/<place_id>')
    api.add_resource(AdminReviewModify, '/api/v1/reviews/<review_id>')
    # Additional namespaces or resources will be added later.

    return app
