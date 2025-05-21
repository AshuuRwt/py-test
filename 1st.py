from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the API mother fucker!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in data if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

# POST (add new user)
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    data.append(new_user)
    return jsonify(new_user), 201

# PUT (update user)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in data if u["id"] == user_id), None)
    if user:
        updates = request.get_json()
        user.update(updates)
        return jsonify(user)
    return ("User not found", 404)

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global data
    data = [u for u in data if u["id"] != user_id]
    return ("Deleted", 204)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

