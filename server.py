from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_cors import CORS, cross_origin  # Import CORS

from login import forgotPassword, register as reg
from login import login as log
from login import charity
from login import forgotPassword
from login import resetPassword as reset
import organizations as org
import profiles


# Dummy data to simulate user database
users = {
    'john@example.com': {
        'password': 'Password123!',
        'first_name': 'John',
        'last_name': 'Doe',
        'state': 'CA'
    }
}

# App
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})



app = Flask(__name__)
CORS(app)  # Apply CORS to your Flask app

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')  # Safely retrieve email from data
    password = data.get('password')  # Safely retrieve password from data
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    state = data.get('state')
    security = data.get('security')
    name = f"{firstname} {lastname}"
    
    if reg(email, password, security, firstname, lastname, state):
        profiles.createProfile(email, '', 'profile-pic.png')
        return jsonify({'message': 'Registration successful!', 'status': 200, 'token': email, 'name': name}), 200
    else:
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/registerOrg', methods=['POST'])
def registerOrg():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')
    addr = data.get('addr')
    orgType = data.get('orgType')
    bio = data.get('bio')
    if org.charity_register(name,email,password,phone,addr,orgType,bio):
        # Create Profile
        profiles.createProfile(email, bio, 'profile-pic.png')
        # User authenticated, return success response
        return jsonify({'message': 'Registration successful!', 'status': 200, 'token': email, 'name':name}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if log(email,password):
        # User authenticated, return success response
        return jsonify({'message': 'Signin successful!', 'status': 200, 'token': email, 'name': profiles.getName(email), 'charity':charity(email), 'pfp':profiles.getPFP(email)}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/resetPassword', methods=['POST'])
def resetPassword():
    data = request.get_json()
    email = data.get('email')
    security = data.get('security')
    password = data.get('password')

    if forgotPassword(email,security):
        # User authenticated, reset password and return success response
        reset(email, password)
        return jsonify({'message': 'Reset successful!', 'status': 200, 'token': email, 'name': profiles.getName(email), 'charity':charity(email), 'pfp':profiles.getPFP(email)}), 200
    else:
        # Incorrect email or security answer
        return jsonify({'error': 'Incorrect email or security answer'}), 401
    
@app.route('/getProfile', methods=['POST'])
def getProfile():
    data = request.get_json()
    email = data.get('email')

    if profiles.getEntireProfile(email):
        ret = profiles.getEntireProfile(email)
        # User authenticated, return success response
        return jsonify({'message': 'Request successful!', 'status': 200, 'token': email, 'ret':ret}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    email = data.get('email')
    updateType = data.get('updateType')
    update = data.get('update')

    if updateType=='all':
        if profiles.update(email,update):
            # User authenticated, return success response
            return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
        else:
            # Incorrect email or password
            return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/updateFirstName', methods=['POST'])
def updateFirstName():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateFirstName(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/updateLastName', methods=['POST'])
def updateLastName():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateLastName(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/updateAddress', methods=['POST'])
def updateAddress():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateAddress(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/updateBio', methods=['POST'])
def updateBio():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateBio(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/updatePFP', methods=['POST'])
def updatePFP():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updatePFP(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    searchText = data.get('searchText')
    charities = org.charity_search(searchText)
    
    if ch:
        return jsonify({'message': 'Registration successful!', 'status': 200, 'charities':5}), 200
    else:
        return jsonify({'error': 'Incorrect email or password'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5001)
