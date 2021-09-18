import './App.css';
import React from "react";
import Title from './components/title';
import TextBox from './components/textbox';
import Result from './components/result';

const App:React.FC = () => {
  const [val, setVal] = React.useState<String>('')
  const [percentage, setPercentage] = React.useState(0)

  const evalResult = (val: String) => {
    setVal(val)
    console.log("fetch result for "+val)
  }

  return (
    <div className="App">
      <Title />
      <TextBox evalResult={evalResult}/>
      <Result percentage = {percentage}/>
    </div>
  );
}

export default App;
