import './App.css';
import React from "react";
import Title from './components/title';
import TextBox from './components/textbox';
import Result from './components/result';

const axios = require('axios').default;

const App:React.FC = () => {
  const [val, setVal] = React.useState<String>('')
  const [percentage, setPercentage] = React.useState(0)

  const evalResult = (val: String) => {
    setVal(val)
    axios.post('http://localhost:5000/text', {
      'text':val
    }).then( (res:any) => {
        console.log(res.data.val)
        setPercentage(Number(res.data.val))
      })
      .catch((err:any) => console.log("error "+err))
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
