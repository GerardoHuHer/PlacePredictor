import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from "axios";

// Componentes utilizados
import { Panel } from 'primereact/panel';

// Hooks necesarios
import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";

import getUrl from "../../GetUrl"

// Importación de regresión.css
import "./Regresion.css"

// estilos de primereact
import 'primereact/resources/themes/lara-light-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';


export default function Regresion({ respuesta, setRuta }) {
  // Lugar al que quiero llegar
  const [destino, setDestino] = useState("");

  // Hooks para almacenar los lugares
  const [lugares, setLugares] = useState([]);

  // Hook para hacer la petición con el hook useForm
  const { register, handleSubmit, watch, formState: { errors } } = useForm();

  // Petición post para enviar la información a la base de datos
  const onSubmit = async (data) => {
    data.destino = destino;
    console.log("Data: ", data)
    try {
      const response = await axios.post(getUrl() + "/ruta_ideal", data, {headers: {
        "Content-Type": "application/json"
      }});
      setRuta(response)
      console.log("Response: ", response);
    } catch (e) {
      console.log("Error al hacer la petición");
    }
  }

  const onError = (e) => {
    console.log("onError");
  }


  // Hook useEffect para hacer la petición al backend
  useEffect(() => {
    axios.get(getUrl() + "/get_places").then(response => {
      setLugares(response.data);
    }).catch(err => {
      console.log("Error al traer la información de lugares: ", err);
      setLugares(["Sin Información por el momento"])
    });
  }, [])

  return <>
    <div className="mt-3">
      <Panel header="Opciones">
        <form onSubmit={handleSubmit(onSubmit, onError)}>
          <select className="form-select" {...register("origen", {
            required: {
              value: true,
              message: "Es necesario seleccionar un lugar de origen."
            }
          })}>
            <option value="">¿Dónde estás en este momento?</option>
            {lugares?.map(p => {
              return <option key={p._id} value={p.id}>{p.name}</option>
            })}
          </select>

          {errors?.origen?.type === 'required' && (
            <p className="warning-message">{errors.origen.message}</p>
          )}
          <div className="row">
            <div className="col">Nombre</div>
            <div className="col">Conectores</div>
            <div className="col">Comida</div>
            <div className="col">Cantidad</div>
            <div className="col">Botón</div>
          </div>
          {respuesta?.map((res) => {
            return <div className="row">
              <div className="col">
                <p>{res.name}</p>
              </div>
              <div className="col">
                <p>{res.conectores ? "Sí hay conectores" : "No hay conectores"}</p>
              </div>
              <div className="col">
                <p>{res.comida ? "Puedes comer" : "No puedes comer"}</p>
              </div>
              <div className="col">
                <p>{res.cantidad}</p>
              </div>
              <div className="col">
                <button className="btn btn-primary" type="submit" onClick={() => { return setDestino(res.id) }}>¿Cómo llegar?</button>
              </div>
            </div>
          })}
        </form>
      </Panel>
    </div>
  </>
}
