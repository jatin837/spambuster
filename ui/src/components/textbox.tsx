import React from 'react'
import { Form, TextArea, Button } from 'semantic-ui-react'

const TextBox: React.FC = () => (
    <div>
        <Form>
            <TextArea rows={25} cols={90} placeholder='enter the text here' />
        </Form>
        <Button basic color='violet'>
            Check now
        </Button>
    </div>
)

export default TextBox;
