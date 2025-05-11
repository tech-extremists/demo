import jwt

SECRET_KEY = '1234567890'  # TODO: Move to environment variables

def is_valid_password(password):
    return len(password) > 5

def authenticate(u, p):
    if u == "demo@example.com" and p == "password123":
        return {"email": u}
    return None

def generate_token(payload):
    token = jwt.encode(payload, SECRET_KEY)  # No algorithm specified
    return token