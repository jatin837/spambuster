import React from "react";
import { Container } from 'semantic-ui-react'

interface Props {
    percentage: Number,
}

const Result: React.FC<Props> = ({percentage}: Props) => {
    if (percentage === 0){
        console.log("Percentage to be determined")
        return (
            <div>
            </div>
        )
    }else{
        return (
            <Container text>
                <p>
                    <b>{percentage}%</b>
                </p>
            </Container>
        )
    }
}

export default Result;