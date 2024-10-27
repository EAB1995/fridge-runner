import logo from './logo.svg';
import './App.css';
import InputField from './components/insert'; 
import React, { useState } from 'react';

function App() {

    const [response, setResponse] = useState('');

    const triggerLambda = async () => {
        try {
            const res = await fetch('http://localhost:3001/hello');
            const data = await res.json();
            setResponse(data.message);
        } catch(error) {
            console.error('Error triggering Lambda:', error);
            setResponse('Error triggering Lambda');        
        }
    }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>FRIDGE RUNNER</p>
        <p>ETIENNE</p>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <InputField />
        <button onClick={triggerLambda}>Hello World Test</button>
        {response && <p>Lambda Response: {response}</p>}
      </header>
    </div>
  );
}

export default App;
