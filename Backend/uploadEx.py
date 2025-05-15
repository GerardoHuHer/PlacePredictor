import platform
import subprocess
import os
from bson import json_util
import pandas as pd


df = pd.read_csv("./ocupacion_zonas_3000.csv")


print("Subiendo la información..")
try:
    for index, row in df.iterrows(): 
        d = {
            "ocupado": row["ocupado"],
            "dia": row["dia"],
            "hora": row["hora"],
            "id_lugar": row["objid"]

        }
        json_data = json_util.dumps(d)  # convertir a JSON string
        result = subprocess.run([
                    "curl",
                    "-H", "Content-Type: application/json",
                    "-d", json_data,
                    "-X", "POST",
                    "http://localhost:5000/create_information" 
                ], capture_output=True, text=True)
        print("Status:", result.returncode)
        print("Output:", result.stdout)
        print("Error:", result.stderr)
except Exception as e: 
    print("There was an error: ", e)

