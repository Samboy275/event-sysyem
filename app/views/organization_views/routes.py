from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db import get_db
from bson import ObjectId



@jwt_required()
def create_organization():

    if request.method == "POST":
        data = request.get_json()

        name = data.get("name")
        description = data.get("description")

        user = get_jwt_identity()

        db = get_db()

        org_collection = db.organizations
        user_collection = db.users

        admin_user = user_collection.find_one({"email" : user})

        result = org_collection.insert_one({
            "name" : name,
            "description" : description,
            "members" : [
                {"name" : admin_user["name"],
                "email": admin_user["email"],
                "access_level":"admin"},
            ]
        })

        return jsonify(organization_id = str(result.inserted_id)), 201





@jwt_required()
def get_organization(organization_id):

    if request.method == "GET":
        db = get_db()
        try:
            org_id = ObjectId(organization_id)
        except Exception as e:
            return jsonify({"message" : "invalid ID format"}), 400
        org_collection = db.organizations

        org = org_collection.find_one({"_id" : org_id})

        if org is None:
            return jsonify(message="Organization is not registered"), 404

        return jsonify({
            "organization_id" : str(org["_id"]),
            "name" : org["name"],
            "description" : org["description"],
            "members" : org["members"]
        }), 200
