import logo from './logo.svg';
import './App.css';
import InputField from './components/insert'; 
import React, { useState } from 'react';

function App() {

    const [response, setResponse] = useState('');

    const helloWorldLambda = async () => {
        try {
            const res = await fetch('http://127.0.0.1:3001/hello');
            const data = await res.json();
            setResponse(data.message);
        } catch(error) {
            console.error('Error triggering Lambda:', error);
            setResponse('Error triggering Lambda');        
        }
    }

    const saveInputLambda = async () => {
        try {
            const res = await fetch('http://127.0.0.1:3001/save-input', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    ItemId: "2",
                    TestValue: "SampleData2"
                })
            })

            if (!res.ok) {
                throw new Error(`Server error: ${res.status}`);
            }

            const data = await res.json();
            console.log('Response data:', data);
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
        <button onClick={helloWorldLambda}>Hello World Test</button>
        {response && <p>Lambda Response: {response}</p>}
        <InputField />
        <button onClick={saveInputLambda}>Save input Test</button>
        {response && <p>Lambda Response: {response}</p>}
      </header>
    </div>
  );
}

export default App;
