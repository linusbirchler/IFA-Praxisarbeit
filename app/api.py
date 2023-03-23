#Eigenentwicklung
from app import app
from app.models import User, Cleaning
from flask import jsonify

@app.route('/api/users/<id>', methods=['GET'])
def get_users(id):
    data = User.query.get_or_404(id).to_dict()
    return jsonify(data)

@app.route('/api/users', methods=['GET'])
def get_users2():
    data = User.to_collection()
    return jsonify(data)

@app.route('/api/cleaning/<id>', methods=['GET'])
def get_cleaning(id):
    data2 = Cleaning.query.get_or_404(id).to_dict()
    return jsonify(data2)

@app.route('/api/cleaning', methods=['GET'])
def get_cleaning2():
    data2 = Cleaning.to_collection()
    return jsonify(data2)
