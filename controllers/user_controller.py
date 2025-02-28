from flask import Flask, request, jsonify
from services.user_service import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify([user.__dict__ for user in users]), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user.__dict__), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ('firstName', 'lastName', 'birthYear', 'group')):
        return jsonify({'error': 'Invalid input'}), 400
    user_id = user_service.create_user(data['firstName'], data['lastName'], data['birthYear'], data['group'])
    return jsonify({'id': user_id}), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.get_json()
    if not data or not all(key in data for key in ('firstName', 'lastName', 'birthYear', 'group')):
        return jsonify({'error': 'Invalid input'}), 400
    if user_service.update_user(user_id, data['firstName'], data['lastName'], data['birthYear'], data['group']):
        return jsonify({'message': 'User updated'}), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
