import { func } from 'prop-types';
import React, {useState} from 'react';

function App() {
  const [index, setIndex] = useState(0);
  const handleAdd = () => {
    setIndex(index+1);
  };
  const handleSub = () => {
    setIndex(index-1);
  };
  const reset = () => {
    setIndex(0);
  };

  return (
    <>
      <button onClick={handleAdd}>+</button>
      <button onClick={handleSub}>-</button>
      <button onClick={reset}>Reset</button>
      <h2>{index}</h2>
    </>
  );
}

export default App;