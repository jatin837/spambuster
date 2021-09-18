import React from 'react'
import { Form, TextArea, Button } from 'semantic-ui-react'

interface Props {
    evalResult(val: String):void,
}

const TextBox: React.FC<Props> = ({evalResult}) => {
    const [value, setValue] = React.useState('')

    const handleChange = (e:any) => {;
        console.log(e.target.value);
		setValue(e.target.value);
    }

    const handleSubmit = () => {
        console.log("submiting "+value)
        evalResult(value)
    }

    return (
        <div>
            <Form onSubmit = {handleSubmit}>
                <TextArea placeholder='enter the text here' onChange={handleChange}/>
                <Button basic color='violet'>
                    Check now
                </Button>
            </Form>
        </div>
    )
}

export default TextBox;
