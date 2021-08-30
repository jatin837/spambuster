import React from 'react'
import { Form, TextArea, Button } from 'semantic-ui-react'

const TextBox: React.FC = () => {
    const handleSubmit = () => {console.log("submiting, do something about it")}
    return (
        <div>
            <Form onSubmit = {handleSubmit}>
                <TextArea placeholder='enter the text here' />
                <Button basic color='violet'>
                    Check now
                </Button>
            </Form>
        </div>
    )
}

export default TextBox;
