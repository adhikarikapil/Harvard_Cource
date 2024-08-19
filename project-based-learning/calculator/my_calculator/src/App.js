import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="calculator">
        <div id="display" className="row"></div>
        <div id="clear" className="row">AC</div>
        <div id="seven">7</div>
        <div id="seven">8</div>
        <div id="seven">9</div>
        <div id="seven">*</div>
        <div id="seven">4</div>
        <div id="seven">5</div>
        <div id="seven">6</div>
        <div id="seven">/</div>
        <div id="seven">1</div>
        <div id="seven">2</div>
        <div id="seven">3</div>
        <div id="seven">+</div>
        <div id="seven">0</div>
        <div id="seven">.</div>
        <div id="seven">=</div>
        <div id="seven">-</div>
      </div>
    </div>
  );
}

export default App;
