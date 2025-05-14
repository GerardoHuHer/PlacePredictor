from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from flask_cors import CORS
app = Flask(__name__)

# Conexión a la base de datos
connection: str = "mongodb+srv://xayilgph:kvwiW6FmLWw9HCi@pilot.q5evx34.mongodb.net/PLACEPREDICTOR_DB?retryWrites=true&w=majority&appName=Pilot"
app.config["MONGO_URI"] = connection

mongo = PyMongo(app)

CORS(app)

try:
    mongo.cx.server_info()
    print("Conectado a BD")
except Exception as e:
    print(f"Error al conectar: {e}")

# xayilgph
# kvwiW6FmLWw9HCi