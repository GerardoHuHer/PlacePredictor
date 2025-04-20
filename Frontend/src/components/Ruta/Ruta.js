import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

import axios from "axios"

import { Panel } from 'primereact/panel';

export default function Ruta({ ruta }) {

  return <>
    <div className="mt-3 mb-5">
      <Panel header="Ruta">
        {ruta === null ? <p>No se ha seleccionado una ruta</p> : ""}
        {ruta?.map(r => {
          return <div></div>
        })}
      </Panel>
    </div>
  </>
}

