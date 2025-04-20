import React from 'react';
import Filtros from './components/Filtros/Filtros'; 
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className='container'>
    <h1 className='mt-3'>Place Predictor</h1>
      <Filtros/>
    </div>
  );
}

export default App;
