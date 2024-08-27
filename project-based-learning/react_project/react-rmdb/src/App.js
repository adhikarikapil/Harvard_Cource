import React from "react";

// Components
import Header from "./components/Header/headerIndex";
import Home from './components/HomePage/Home'

// Styles
import { GlobalStyles } from "./GlobalStyles";

function App() {
  return (
    <div className="App">
      <Header />
      <Home /> 
      <GlobalStyles />
    </div>
  );
}

export default App;
