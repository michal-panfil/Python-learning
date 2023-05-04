from flask import Flask, request, jsonify
app = Flask(__name__)

users = [
 {"id": 1, "name": "John Doe"},
 {"id": 2, "name": "Jane Doe"},
 {"id": 3, "name": "John Smith"},
]

def _find_next_id():
    return max([user["id"] for user in users]) + 1

@app.get("/users")
def get_users():
    return jsonify(users)

@app.post("/users")
def add_user():
    if request.is_json:
        user = request.json
        if("name" not in user):
            return {"error": "Missing name"}, 400

        user["id"] = _find_next_id()
        users.append(user)
        return jsonify(user), 201
    return {"error": "Request must be JSON"}, 415

#$env:FLASK_APP="api.py'
# pyhton -m flask run