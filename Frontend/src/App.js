import React from 'react';

// Componente creados manualmente
import Filtros from './components/Filtros/Filtros'; 
import Regresion from "./components/Regresion/Regresion"
import Ruta from "./components/Ruta/Ruta"

// Estilos de bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';

// importación de Hooks para almacenar la respuesta
import { useState } from 'react';

function App() {

  const [respuesta, setRespuesta] = useState(null);
  const [ruta, setRuta] = useState(null);  

  return (
    <div className='container'>
    <h1 className='mt-3'>Lugares libres</h1>
      <Filtros setRespuesta={setRespuesta}/>
      <Regresion respuesta={respuesta} setRuta={setRuta}/>
      <Ruta ruta={ruta}/>
    </div>
  );
}

export default App;
