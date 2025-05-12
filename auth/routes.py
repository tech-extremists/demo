from flask import Blueprint, request, jsonify
from auth.utils import authenticate, generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Get the JSON data from the request
    data = request.get_json()
    # Authenticate the user using the provided email and password
    user = authenticate(data.get('email'), data.get('password'))
    if user:
        # Generate a token for the authenticated user
        token = generate_token(user)
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/profile', methods=['GET'])
def profile():
    # TODO: Add token validation
    return jsonify({'username': 'demo_user', 'email': 'demo@example.com'})