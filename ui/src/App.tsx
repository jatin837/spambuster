import './App.css';
import React from "react";
import Title from './components/title';
import TextBox from './components/textbox';
import About from './components/about';

const App:React.FC = () => {
  return (
    <div className="App">
      <Title/>
      <TextBox/>
    </div>
  );
}

export default App;
