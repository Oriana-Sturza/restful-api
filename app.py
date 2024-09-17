
---

### **4. RESTful API**

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    """
    Initializes the SQLite database and creates the 'users' table if it doesn't exist.
    """
    with sqlite3.connect("users.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         name TEXT NOT NULL, 
                         email TEXT NOT NULL)''')

@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieves all users from the database.
    Returns:
        list: A list of users in JSON format.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    """
    Adds a new user to the database.
    Request data should be in JSON format with 'name' and 'email'.
    """
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "User added!"})

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Updates an existing user in the database.
    Request data should be in JSON format with 'name' and 'email'.
    """
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()
    conn.close()

    return jsonify({"message": "User updated!"})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Deletes a user from the database based on their ID.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "User deleted!"})

if __name__ == "__main__":
    init_db()  # Initialize the database
    app.run(debug=True)
