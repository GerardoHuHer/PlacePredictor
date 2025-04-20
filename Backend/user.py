from flask import jsonify, request, Response
from database import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]
    if username and email and password: 
        hashed_password = generate_password_hash(password)
        user_data: dict = {
            "username": username, 
            "password": hashed_password, 
            "email": email
        } 
        result = mongo.db.users.insert_one(user_data)
        response = {
            "id": str(result.inserted_id), 
            "username": username,
            "email": email,
            "password": hashed_password
        }
        return response
    else: 
        return not_found()
    return {"message": "received"}

@app.route("/delete_user/<id>", methods=["DELETE"])
def delete_user(id):
    mongo.db.users.delete_one({"_id": ObjectId(id)})
    response = jsonify({"message": f"El usuario con el id {id} fue eliminado exitosamente."})
    return response

@app.route("/get_users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")

@app.route("/update_user/<id>", methods=["PUT"])
def update_user(id):
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]
    if username and password and email:
        hashed_password:str = generate_password_hash(password)
        mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": {
                                      "username": username, 
                                      "password": hashed_password
                                  }})
        response = jsonify({"message": f"El usuario con el {id} fue actualizado exitosamente."})
        return response

@app.route("/get_user/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")
