from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return jsonify({
            "success": True,
            "message": "Login successful"
        })
    else:
        return jsonify({
            "success": False,
            "message": "Invalid username or password"
        }), 401

if __name__ == '__main__':
    app.run(debug=True)
