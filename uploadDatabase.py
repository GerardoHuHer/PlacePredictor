import platform
import subprocess
import os
from bson import json_util

informacion: list[dict] = []

# information = [{
#     "id": 3, 
#     "name": "Prueba",
#     "comida": True,
#     "conectores": False,
#     "cantidad": 5
# },{
#     "id": 4, 
#     "name": "Prueba1",
#     "comida": False,
#     "conectores": False,
#     "cantidad": 5
# }]

print("Subiendo la información..")
try:
    for d in informacion: 
        d = json_util.dumps(d)

        result = subprocess.run([
                    "curl",
                    "-H", "Content-Type: application/json",
                    "-d", d,
                    "-X", "POST",
                    "http://localhost:5000/create_place" 
                ], capture_output=True, text=True)
        print("Status:", result.returncode)
        print("Output:", result.stdout)
        print("Error:", result.stderr)
except Exception as e: 
    print("There was an error: ", e)

