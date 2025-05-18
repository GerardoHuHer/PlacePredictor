# neural_network.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from datetime import datetime
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from database import mongo

model = None
le = None
scaler = None

# Convertir hora a minutos
def hora_a_minutos(hora_str):
    t = datetime.strptime(hora_str, "%H:%M")
    return t.hour * 60 + t.minute

# Entrenar modelo
def entrenar_modelo():
    global model, le, scaler
    data = list(mongo.db.information.find())
    df = pd.DataFrame(data)
    df = df.drop(columns=['_id'], errors='ignore')
    df = df.dropna(subset=['hora', 'dia', 'lugar', 'ocupado'])

    df['minutos'] = df['hora'].apply(hora_a_minutos)

    le = LabelEncoder()
    df['lugar_encoded'] = le.fit_transform(df['lugar'])

    X = df[['dia', 'minutos', 'lugar_encoded']]
    y = df['ocupado'].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train[['dia', 'minutos']] = scaler.fit_transform(X_train[['dia', 'minutos']])
    X_test[['dia', 'minutos']] = scaler.transform(X_test[['dia', 'minutos']])

    model = Sequential([
        Dense(16, activation='relu', input_shape=(3,)),
        Dense(64, activation='relu'),
        Dense(64, activation='relu'),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    # model.fit(X_train, y_train, epochs=500, batch_size=9, verbose=1)
    model.fit(X_train, y_train, epochs=1000, batch_size=9, verbose=1)

    print("Modelo entrenado")

# Predicción
def predecir_ocupacion(dia, hora_str, lugar_str):
    global model, le, scaler
    if model is None:
        raise Exception("No se ha entrenado el modelo")

    minutos = hora_a_minutos(hora_str)
    lugar_encoded = le.transform([lugar_str])[0]
    datos = np.array([[dia, minutos]])
    datos = (datos - scaler.mean_[:2]) / scaler.scale_[:2]
    entrada = np.hstack([datos, [[lugar_encoded]]])
    prediccion = model.predict(entrada)[0][0]
    return prediccion >= 0.5
