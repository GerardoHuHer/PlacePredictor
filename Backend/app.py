from flask import jsonify, request, Response
from database import mongo, app
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from user import *


@app.route("/")
def hello(): 
    return "hello, world!"

@app.route("/create_place", methods=["POST"])
def create_place():
    id: int = request.json["id"]
    name = request.json["name"]
    comida = request.json["comida"]
    conectores = request.json["conectores"]
    cantidad = request.json["cantidad"]
    place_data = {
        "id": id,
        "name": name,
        "comida": comida,
        "conectores": conectores,
        "cantidad": cantidad
    }
    try:
        result = mongo.db.places.insert_one(place_data)
        response = {"message": f"{name} fue creado exitosamente"}
        return response
    except: 
        not_found()
        return


@app.route("/get_places", methods=["GET"])
def get_places():
    places = mongo.db.places.find()
    response = json_util.dumps(places)
    return Response(response, mimetype="application/json") 

@app.errorhandler(404) 
def not_found(err=None):  
    response = jsonify({
        "message": "Recurso no encontrado: " + request.url,
        "status": 404
    })
    response.status_code = 404
    return response

if __name__ == "__main__":  
    app.run(debug=True, host="0.0.0.0", port=5000)
