from flask import jsonify, request, Response
from database import mongo, app
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from user import *
from flask_cors import CORS
from functions import dfs

CORS(app)

@app.route("/")
def hello(): 
    return "hello, world!"

# Endpoint post filtros
@app.route("/post_filtros", methods=["POST"])
def post_filtros():
    data = request.get_json()
    cantidad: int = data["cantidad"]
    comida = data["comida"]
    conectores = data["conectores"]
    query = {"cantidad": cantidad}
    if comida != 2:
        query["comida"] = comida
    if conectores != 2: 
        query["conectores"] = conectores
    try: 
        result = mongo.db.information.find(query)
        response = json_util.dumps(result)
        return response
    except Exception as e:
        response = json_util.dumps({"message": f"There are not a place with that characteristics, {e}" })
        return response, 500

@app.route("/create_information", methods=["POST"])
def create_information(): 
    data = request.get_json()
    # Información que vamos a subir a la base de datos
    name = data["name"] # Nombre del lugar
    dia = data["dia"] # Día, (lunes, 0), (martes, 1) ...
    hora = data["hora"] # Hora 
    conector = data["conector"] # bool si tiene conector
    comida = data["comida"] # bool si puedes comer
    cantidad = data["cantidad"] # Cantidad de personas que pueden estar
    lugar = data["id_lugar"] # ObjectId del lugar
    information_data: dict = {
        "name": name,
        "dia": dia,
        "hora": hora,
        "conector": conector,
        "comida": comida,
        "cantidad": cantidad,
        "lugar": lugar
    }
    try:
        result = mongo.db.information.insert_one(information_data)
        response = {"message": f"{name} fue creado exitosamente"}
        return response
    except: 
        not_found()
        return ""

@app.route("/create_place", methods=["POST"])
def create_place():
    data = request.get_json()
    id: int = data["id"]
    name = data["name"]
    comida = data["comida"]
    conectores = data["conectores"]
    cantidad = data["cantidad"]
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
        return ""

@app.route("/get_places", methods=["GET"])
def get_places():
    places = mongo.db.places.find()
    response = json_util.dumps(places)
    return Response(response, mimetype="application/json") 

@app.route("/ruta_ideal", methods=["POST"])
def ruta_ideal():
    data = request.get_json()
    destino = data["destino"]
    origen = data["origen"]
    try:        
        camino = dfs(inicio=origen, objetivo=destino)
        if camino:
            for cam in camino:
                print(' -> '.join(cam))
            return ""
        else:
            return ""
    except Exception as e: 
        return {"message": f"There was an error looking for paths"}

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
