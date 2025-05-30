// Importaciones de react, y estilos de bootstrap
import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

// Hooks y componentes a usar
import { useForm } from "react-hook-form";
import { Panel } from 'primereact/panel';

// Dependencias necesarias
import axios from "axios";


// estilos de primereact
import 'primereact/resources/themes/lara-light-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';

// estilos personalizados
import "./Filtros.css"

// Importación de la función getUrl()
import getUrl from "../../GetUrl"



export default function Filtros({ setRespuesta }) {

  // Hook para hacer la petición con el hook useForm
  const { register, handleSubmit, watch, formState: { errors } } = useForm();

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

  // Objeto de opciones para comida y conectores
  const opciones = [
    { "text": "Sí", "value": true },
    { "text": "No", "value": false },
    { "text": "Cualquiera de las opciones", "value": 2 },
  ]

  // Petición post para enviar la información a la base de datos
  const onSubmit = async (data) => {
    let com;
    let con;
    if (data.comida === "true") {
      com = true;
    } else {
      if (data.comida === "false") {
        com = false
      } else {
        com = 2
      }
    }
    if (data.conectores === "true") {
      con = true;
    } else {
      if (data.conectores === "false") {
        con = false
      } else {
        con = 2
      }
    }
    const parsedData = {
      personas: parseInt(data.personas),
      comida: com,
      conectores: con,
    }
    console.log("Data", parsedData);
    try {
      const response = await axios.post(getUrl() + "/post_filtros", parsedData);
      console.log("response: ", response)
      if (response.data.length > 0) {
        setRespuesta(response.data);
      } else {
        alert("No se econtraron lugares con esas caracteristicas")
      }

    } catch (e) {
      console.log("Error al hacer la petición");
    }
  }

  const onError = (e) => {
    console.log("onError");
  }

  return <>
    <div className="mt-5">
      <Panel header="Filtros">
        <form onSubmit={handleSubmit(onSubmit, onError)} >
          <div className="row filtros">
            <div className="col">
              <select className="form-select select-filtros" {...register("personas", {
                required: {
                  value: true,
                  message: "Cantidad de personas requeridas."
                }
              })}>
                <option value="">Cantidad de Personas</option>
                {cantidades.map((opc) => {
                  return <option value={opc.id}>{opc.cantidad}</option>
                })}
              </select>
              {errors?.cantidad?.type === 'required' && (
                <p className="warning-message">{errors.cantidad.message}</p>
              )}
            </div>
            <div className="col">
              <select className="form-select select-filtros" {...register("conectores", {
                required: {
                  value: true,
                  message: "Seleccione una opción por favor."
                }
              })}>
                <option value="">Conectores</option>
                {opciones.map((opc) => {
                  return <option value={opc.value}>{opc.text}</option>
                })}
              </select>
              {errors?.conectores?.type === 'required' && (
                <p className="warning-message">{errors.conectores.message}</p>
              )}
            </div>
            <div className="col">
              <select className="form-select select-filtros" {...register("comida", {
                required: {
                  value: true,
                  message: "Seleccione una opción por favor."
                }
              })}>
                <option value="">Comida</option>
                {opciones.map((opc) => {
                  return <option value={opc.value}>{opc.text}</option>
                })}
              </select>
              {errors?.comida?.type === 'required' && (
                <p className="warning-message">{errors.comida.message}</p>
              )}
            </div>
            <div className="col">
              <button type="submit" className="btn btn-primary select-filtros">Buscar</button>
            </div>
          </div>
        </form>
      </Panel>
    </div>
  </>
}
