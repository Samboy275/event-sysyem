from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, get_jwt_identity
from app.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.validators import is_valid_email
import redis
import datetime


def sign_up():
    "Sign up view function"

    if request.method == "POST":
        message = ""
        data = request.get_json()
        # get user data
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        hashed_password = generate_password_hash(password)

        # TODO add user to the database
        db = get_db()
        users_collection = db.users

        existing_user = users_collection.find_one({"email": email})

        if existing_user:
            message = "This email already exists"
            return jsonify({"message" : message})

        if not is_valid_email(email):
            message = "Please use a valid email address"
            return jsonify({"message" : message})

        result = users_collection.insert_one({
            "name" : name,
            "password" : hashed_password,
            "email" : email
        })

        message = f"User with name {name} is created!"

        return jsonify({"message" : message}), 201


redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def sign_in():

    if request.method == "POST":
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        #TODO create access token and refresh token and return them to the user
        db = get_db()

        user = db.users.find_one({"email" : email})

        if not user:
            return jsonify({"message": "User does not exist"}), 401

        if not check_password_hash(user["password"], password):
            return jsonify({"message" : "Incorrect password"}), 401


        access_token = create_access_token(identity=user["email"])
        refresh_token = create_refresh_token(identity=user["email"])

        # redis_client.setex(f"access_token:{access_token}", 3600, "active")
        # redis_client.setex(f"refresh_token:{refresh_token}", 86400, "active")

        return jsonify({
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "message" : "Sign in Successful"
        }), 200



def refresh_token():

    if request.method == "POST":
        data = request.get_json()
        refresh_token = data.get("refresh_token")
        decoded_token = decode_token(refresh_token)

        if "exp" in decoded_token:
            expiration_time = decoded_token["exp"]
            current_time = datetime.datetime.now()

            if expiration_time < current_time.timestamp():
                return jsonify(message="Token has expired")
        user = decoded_token.get("sub")
        refresh_token = create_refresh_token(identity=user)
        access_token = create_access_token(identity=user)

        return jsonify({
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "message" : "Token Refreshed"
        }), 200
