from flask_cors import CORS
from models import *
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session

app = Flask(__name__)
CORS(app, origins="http//localhost:3000") 

@app.route('/users', methods=['POST'])
def createUser():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    new_user = usuarios(name, email, password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

@app.route('/users', methods=['GET'])
def getUsers():
    users = usuarios.query.all()
    print(users)
    output = []
    for user in users:
        user_data = {}
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['password'] = user.password
        output.append(user_data)
    return jsonify(output)

@app.route('/users/<name>', methods=['GET'])
def getUser(name):
    user = usuarios.query.get(name)
    return jsonify(user.serialize())


@app.route('/users/<name>', methods=['DELETE'])
def deleteUser(name):
    user = usuarios.query.get(name)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted!'})

@app.route('/users/<name>', methods=['PUT'])
def updateUser(name):
    user = usuarios.query.get(name)
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    user.name = name
    user.email = email
    user.password = password
    db.session.commit()
    return jsonify({'message': 'User updated!'})






    



