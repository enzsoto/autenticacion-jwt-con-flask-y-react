"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    required_fields = ["email", "password"]

    missing_fields = []

    for field in required_fields:
        if data.get(field) is None or str(data.get(field)).strip() == "":
            missing_fields.append(field)

    if missing_fields:
        return jsonify({
            "message": "Faltan campos obligatorios",
            "fields": missing_fields
        }), 400

    email = data["email"].strip().lower()
    password = data["password"]

    user = User.query.filter_by(email=email).first()

    if user is None: 
        return jsonify({
            "message": "Credenciales inválidas"
        }), 401
    
    if user.password != password:
        return jsonify({
            "message": "Credenciales inválidas"
        }), 401
    
    access_token = create_access_token(identity=str(user.id))
    
    return jsonify({
        "message": "Login exitoso",
        "token": access_token,
        "user": user.serialize()
    }), 200


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    required_fields = ["email", "password"]

    missing_fields = []

    for field in required_fields:
        if data.get(field) is None or str(data.get(field)).strip() == "":
            missing_fields.append(field)

    if missing_fields:
        return jsonify({
            "message": "Faltan campos obligatorios",
            "fields": missing_fields
        }), 400
    
    email = data["email"].strip().lower()
    password = data["password"]

    user_exists = User.query.filter_by(email=email).first()

    if user_exists: 
        return jsonify({
            "message": "El email ya está registrado"
        }), 409
    
    new_user = User(
        email=email,
        password=password,
        is_active=True
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "message": "Usuario registrado"
    }), 201