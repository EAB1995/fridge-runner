import logo from './logo.svg';
import './App.css';
import InputField from './components/insert'; 
import React, { useState } from 'react';

function App() {

    const [response, setResponse] = useState({
        helloWorldResponse: "", 
        saveInputResponse: "",
        getTestTableResponse:""
    });

    const helloWorldLambda = async () => {
        try {
            const res = await fetch('http://127.0.0.1:3001/hello');
            const data = await res.json();

            setResponse(prevState => ({
                ...prevState,
                helloWorldResponse: data.message
              }));

        } catch(error) {
            console.error('Error triggering Lambda:', error);
            setResponse('Error triggering Lambda');        
        }
    }

    const saveInputLambda = async () => {
        try {
            //Changed line below now that CAM CLI startup is localhost rather than 127.0.0.1
            //const res = await fetch('http://127.0.0.1:3001/save-input', {
            const res = await fetch('http://localhost:3001/save-input', {
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
            
            setResponse(prevState => ({
                ...prevState, saveInputResponse: data.message
            }));

        } catch(error) {
            console.error('Error triggering Lambda:', error);
            setResponse('Error triggering Lambda');        
        }
    }

    const getTestTableLambda = async () => {
        try {
            //Changed line below now that CAM CLI startup is localhost rather than 127.0.0.1
            //const res = await fetch('http://127.0.0.1:3001/save-input', {
            const res = await fetch('http://localhost:3001/get-test-table', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })

            if (!res.ok) {
                throw new Error(`Server error: ${res.status}`);
            }

            const data = await res.json();
            console.log('Response data:', data);
            
            setResponse(prevState => ({
                ...prevState, getTestTableResponse: data.message
            }));

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
        <button onClick={helloWorldLambda}>Hello World Test</button>
        {response.helloWorldResponse && <p>Hello World Test: {response.helloWorldResponse}</p>}
        <InputField />
        <button onClick={saveInputLambda}>Save input Test</button>
        {response.saveInputResponse && <p>Save Input Test: {response.saveInputResponse}</p>}
        <button onClick={getTestTableLambda}>Get Test Table</button>
        {response.getTestTableResponse && <p>Save Input Test: {response.getTestTableResponse}</p>}
      </header>
    </div>
  );
}

export default App;
