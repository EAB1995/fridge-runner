import logo from './logo.svg';
import './App.css';
import InputField from './components/insert'; 

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>FRIDGE RUNNER</p>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <InputField />
      </header>
    </div>
  );
}

export default App;
