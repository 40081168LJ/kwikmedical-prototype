from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

# This is a hardcoded user list for demonstration purposes
# In a real system, you would query this from a database.
users = {
    "admin": {"password": "adminpass", "role": "admin"},
    "operator": {"password": "operatorpass", "role": "operator"}
}

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = users.get(username)
    if user and user['password'] == password:
        # Create JWT access token
        access_token = create_access_token(identity={"username": username, "role": user['role']})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
