// Importaciones de react, y estilos de bootstrap
import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

// Hooks y componentes a usar
import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { Panel } from 'primereact/panel';
import { Accordion, AccordionTab } from 'primereact/accordion';

// Dependencias necesarias
import axios from "axios";


// estilos de primereact
import 'primereact/resources/themes/lara-light-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';

// estilos personalizados
import "./Filtros.css"



export default function Filtros() {

  // Hook para hacer la petición con el hook useForm
  const { register, handleSubmit, watch, formState, errors } = useForm();

  // Hooks para almacenar los lugares
  const [lugares, setLugares] = useState([]);

  // Objeto para cantidad de personas
  const cantidades = [
    { id: 1, cantidad: 1 },
    { id: 2, cantidad: 2 },
    { id: 3, cantidad: 3 },
    { id: 4, cantidad: 4 },
    { id: 6, cantidad: 6 },
    { id: 7, cantidad: 7 },
    { id: 8, cantidad: 8 },
    { id: 9, cantidad: 9 },
    { id: 10, cantidad: 10 },
  ];

  // Hook useEffect para hacer la petición al backend
  // useEffect(() => {
  //   axios.get("").then(response => {
  //     setLugares(response.data);
  //   }).catch(err => {
  //     console.log("Error al traer la información de lugares: ", err);
  //     setLugares(["Sin Información por el momento"])
  //   });
  // }, [])

const onSubmit = async (data) => {
  try {
    // Funciones post
  } catch(e) {
    console.log("Error al hacer la petición");
  }
}

  const onError = (e)=> {
    console.log("onError");
  }

  return <>
    <div className="mt-5">
      <Panel header="Opciones">
        <form onSubmit={handleSubmit(onSubmit, onError)} >
          <div className="row filtros">
            <div className="col">
              <select className="form-select select-filtros" {...register("id_lugar_procedencia", {
                required: {
                  value: true,
                  message: "Lugar de procedencia necesario."
                }
              })}>
                <option>Procedencia</option>
                {lugares.map((place) => {
                  return <option value={place.id}>{place.name}</option>
                })}
              </select>
              {errors?.id_lugar_procedencia?.type === 'required' && (
                <p className="warning-message">{errors.id_lugar_procedencia.message}</p>
              )}
            </div>
            <div className="col">
              <select className="form-select select-filtros " {...register("id_lugar_destino", {
                required: {
                  value: true,
                  message: "Lugar de destino necesario."
                }
              })}>
                <option>Destino</option>
                {lugares.map((place) => {
                  return <option value={place.id}>{place.name}</option>
                })}
              </select>
              {errors?.id_lugar_destino?.type === 'required' && (
                <p className="warning-message">{errors.id_lugar_destino.message}</p>
              )}
            </div>
            <div className="col">
              <select className="form-select select-filtros" {...register("id_cantidad", {
                required: {
                  value: true,
                  message: "Cantidad de personas requeridas."
                }
              })}>
                <option>Cantidad de Personas</option>
                {cantidades.map((opc) => {
                  return <option value={opc.id}>{opc.cantidad}</option>
                })}
              </select>
            {errors?.id_cantidad?.type === 'required' && (
              <p className="warning-message">{errors.id_cantidad.message}</p>
            )}
            </div>
            <div className="col">
              <button type="submit" className="btn btn-primary select-filtros">Buscar</button>
            </div>
          </div>
          <Accordion>
            <AccordionTab header="Más Filtros">
              <div>
                <div className="row" id="encabezado">
                  <div className="col">
                    <b className="text-masfiltros">Característica</b>
                  </div>
                  <div className="col">
                    <b className="text-encabezados">Sí/No</b>
                  </div>
                  <div className="col">
                    <b className="text-encabezados">Descripción</b>
                  </div>
                </div>
                <div className="row" id="conectores">
                  <div className="col">
                    <p className="text-masfiltros">Conectores: </p>
                  </div>
                  <div className="col">
                    <input type="checkbox"></input>
                  </div>
                  <div className="col">
                    <p>Qué el lugar buscado tenga conectores</p>
                  </div>
                </div>
                <div className="row" id="comida">
                  <div className="col">
                    <p className="text-masfiltros">Comida: </p>
                  </div>
                  <div className="col">
                    <input type="checkbox"></input>
                  </div>
                  <div className="col">
                    <p>Permiten comer en el lugar, marca la casilla para buscar un lugar que sí lo permita</p>
                  </div>
                </div>
              </div>
            </AccordionTab>
          </Accordion>
        </form>
      </Panel>
    </div>
  </>
}
