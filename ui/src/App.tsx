import './App.css';
import React from "react";
import Title from './components/title';
import TextBox from './components/textbox';
import Result from './components/result';

const App:React.FC = () => {
  return (
    <div className="App">
      <Title/>
      <TextBox/>
      <Result/>
    </div>
  );
}

export default App;
