# HBnB - Auth & DB
This directory contains the following tasks:

- 0 Modify the Application Factory to Include the Configuration
- 1 Modify the User Model to Include Password Hashing
- 2 Implement JWT Authentication with flask-jwt-extended
- 3 Implement Authenticated User Access Endpoints
- 4 Implement Administrator Access Endpoints
- 5 Implement SQLAlchemy Repository
- 6 Map the User Entity to SQLAlchemy Model
- 7 Map the Place, Review, and Amenity Entities
- 8 Map Relationships Between Entities Using SQLAlchemy
- 9 SQL Scripts for Table Generation and Initial Data
- 10 Generate Database Diagrams

# Objectives of the Project

- Authentication and Authorization: Implement JWT-based user authentication using Flask-JWT-Extended and role-based access control with the is_admin attribute for specific endpoints.
- Database Integration: Replace in-memory storage with SQLite for development using SQLAlchemy as the ORM and prepare for MySQL or other production grade RDBMS.
- CRUD Operations with Database Persistence: Refactor all CRUD operations to interact with a persistent database.
- Database Design and Visualization: Design the database schema using mermaid.js and ensure all relationships between entities are correctly mapped.
- Data Consistency and Validation: Ensure that data validation and constraints are properly enforced in the models.

#Learning Objectives

* Implement JWT authentication to secure your API and manage user sessions.
* Enforce role-based access control to restrict access based on user roles (regular users vs. administrators).
* Replace in-memory repositories with a SQLite-based persistence layer using SQLAlchemy for development and configure MySQL for production.
* Design and visualize a relational database schema using mermaid.js to handle relationships between users, places, reviews, and amenities.
* Ensure the backend is secure, scalable, and provides reliable data storage for production environments.

