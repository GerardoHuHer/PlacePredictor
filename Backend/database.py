from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from flask_cors import CORS
app = Flask(__name__)

# Conexión a la base de datos
connection: str = "mongodb://localhost:27017/placesdb"
app.config["MONGO_URI"] = connection

mongo = PyMongo(app)

CORS(app)


