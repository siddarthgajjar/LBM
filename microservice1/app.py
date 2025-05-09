from flask import Flask, jsonify, request
import jwt
import requests

app = Flask(__name__)

# Cognito configuration (replace with actual values)
COGNITO_REGION = "us-east-1"
COGNITO_USER_POOL_ID = "your-user-pool-id"
JWKS_URL = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{COGNITO_USER_POOL_ID}/.well-known/jwks.json"

# Fetch JWKS for token validation
def get_jwks():
    return requests.get(JWKS_URL).json()

@app.route('/')
def home():
    return jsonify({"message": "Hello from microservice1"})

@app.route('/protected')
def protected():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not token:
        return jsonify({"message": "Token is missing"}), 401
    try:
        jwks = get_jwks()
        # Simplified token validation (use proper JWT decoding in production)
        decoded = jwt.decode(token, jwks['keys'][0], algorithms=["RS256"])
        return jsonify({"message": "Access granted", "user": decoded})
    except Exception as e:
        return jsonify({"message": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)