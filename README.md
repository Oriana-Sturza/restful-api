# RESTful API

A Python Flask-based REST API that supports basic CRUD (Create, Read, Update, Delete) operations for managing user data.

## Features
- Get all users.
- Add a new user.
- Update an existing user.
- Delete a user.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/restful-api.git
   cd restful-api
   ```

   
2. Install the required dependencies:
pip install Flask

3. Run the app:
python app.py

The API will be running at http://127.0.0.1:5000/

API Endpoints:

GET /users: Retrieve all users.

POST /users: Add a new user (requires name and email in the JSON body).

PUT /users/<id>: Update user details (requires name and email in the JSON body).

DELETE /users/<id>: Delete a user by ID.

Example Usage:

1. Get all users: curl -X GET http://127.0.0.1:5000/users

2. Add a new user: curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"name": "John", "email": "john@example.com"}'

Future Improvements:

Add authentication and authorization.

Implement pagination for large datasets.
