from flask import jsonify, request, Response
from database import mongo, app
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from user import *
from flask_cors import CORS
from functions import dfs
from datetime import datetime, timedelta
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import numpy as np
from neural_network import *
import neural_network as nn
from datetime import datetime, timedelta

CORS(app)

@app.route("/")
def hello(): 
    return "hello, world!"

# # Endpoint post filtros
@app.route("/post_filtros", methods=["POST"])
def post_filtros():
    data = request.get_json()
    personas = int(data["personas"])
    comida = data["comida"]
    conectores = data["conectores"]
    query = {"cantidad": {"$gt": personas}, "zona": True}
    if comida != 2:
        query["comida"] = comida
    if conectores != 2: 
        query["conectores"] = conectores
    try: 
        print(query)
        result = mongo.db.places.find(query)
        # response = json_util.dumps(result)
        response = result
        places = list(response)
        if not places:
            return {"message": "No se encontraron lugares con esas caracteristicas", "status": -1}

        information = []
        ahora = datetime.now()
        hora_actual = ahora.strftime("%H:%M")
        dia_actual = ahora.isoweekday() - 1
        for place in places:
            value = nn.predecir_ocupacion(dia_actual, hora_actual ,str(place["_id"]))
            place["ocupado"] = value
        return json_util.dumps(places)
    except Exception as e:
        response = json_util.dumps({"message": f"There are not a place with that characteristics, {e}" })
        return response, 500

@app.route("/create_information", methods=["POST"])
def create_information(): 
    data = request.get_json()
    # Información que vamos a subir a la base de datos
    ocupado = data["ocupado"] # Nombre del lugar
    dia = data["dia"] # Día, (lunes, 0), (martes, 1) ...
    hora = data["hora"] # Hora 
    lugar = data["id_lugar"] # ObjectId del lugar
    information_data: dict = {
        "ocupado": ocupado,
        "dia": dia,
        "hora": hora,
        "lugar": lugar
    }
    try:
        result = mongo.db.information.insert_one(information_data)
        response = {"message": f"{lugar} fue creado exitosamente"}
        return response
    except: 
        not_found()
        return ""

@app.route("/create_place", methods=["POST"])
def create_place():
    data = request.get_json()
    id: int = data["id"]
    leyenda = data["Leyenda"]
    # comida = data["Comida"] if data["Comida"] != None else False
    comida = data.get("Comida", False)
    conectores = data.get("Conectores", False)
    cantidad = data.get("Personas", 0)
    location = data["location"]
    zona = data["Zona"]
    place_data = {
        "id": id,
        "name": leyenda,
        "comida": comida,
        "conectores": conectores,
        "cantidad": cantidad,
        "zona": zona
    }
    try:
        result = mongo.db.places.insert_one(place_data)
        response = {"message": f"{leyenda} fue creado exitosamente"}
        return response
    except: 
        not_found()
        return ""

@app.route("/get_places", methods=["GET"])
def get_places():
    # places = mongo.db.places.find()
    places = mongo.db.places.find({"zona": True})
    response = json_util.dumps(places)
    return Response(response, mimetype="application/json") 

@app.route("/ruta_ideal", methods=["POST"])
def ruta_ideal():
    data = request.get_json()
    destino = data["destino"]
    origen = data["origen"]
    if destino == " ":
            return {"message": "No se ingreso el destino", "status": -1}
    try:        
        camino = []
        camino = dfs(inicio=origen, objetivo=destino)
        # camino = dfs(inicio="Z9", objetivo="Z1")
        if camino:
            return {"message": "Camino encontrado con exito", "path": camino}
        else:
            return {"message": "No se encontro un camino", "path": []}
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




def redondear_a_media_hora():
    ahora = datetime.now()
    minutos = ahora.minute

    # Si los minutos son mayores a 0, redondeamos
    if minutos == 0 or minutos == 30:
        redondeada = ahora.replace(minute=0 if minutos == 0 else 30, second=0, microsecond=0)
    elif minutos < 30:
        redondeada = ahora.replace(minute=30, second=0, microsecond=0)
    else:  # minutos > 30
        redondeada = (ahora + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)

    return redondeada.strftime("%H:%M")


def get_day(day: str) -> int: 
    days: dict[str, int] = {
        "Lunes": 0, 
        "Martes": 1, 
        "Miércoles": 2,
        "Jueves": 3, 
        "Viernes": 4, 
        "Sábado": 5
    }

    return days.get(day, -1)
    


if __name__ == "__main__":  
    entrenar_modelo()
    app.run(debug=True, host="0.0.0.0", port=5000)
