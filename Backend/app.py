from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

connection: str = "mongodb://localhost:27017/PlacePredictor"
app.config["MONGO_URI"] = connection

mongo = PyMongo(app)


@app.route("/")
def hello(): 
    return "hello, world!"

@app.route('/lugares', methods=['GET'])
async def obtener_lugares():
    lugares = mongo.db.lugares.find()
    lugares_list = []
    for lugar in lugares: 
        lugar["_id"] = str(lugar["_id"])  # Convertir ObjectId a string
        lugares_list.append(lugar)

    return jsonify(lugares_list)

if __name__ == "__main__":
    app.run(debug=True)
