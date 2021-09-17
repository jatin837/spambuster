import React from 'react'
import { Form, TextArea, Button } from 'semantic-ui-react'

const TextBox: React.FC = () => {
    const [value, setValue] = React.useState('')

    const handleChange = (e:any) => {;
        console.log(e.target.value);
		setValue(e.target.value);
    }

    const handleSubmit = () => {console.log("submiting "+value)}
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
