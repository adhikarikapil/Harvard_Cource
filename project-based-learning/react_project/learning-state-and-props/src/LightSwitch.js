import React from 'react'
import styled from 'styled-components';

const Button = styled.Button`
    position: absolute;
    left: ${props => (props.position === 'left' ? '20px' : '380px')};
    bottom: 20px;
    background: black;
    color: cyan;
    border: 2px solid white;
    border-radius: 10px;
    width: 100px;
    height: 50px;
    cursor: pointer;
`;

const LightSwitch = ({ callback, switchOn, position }) => {
    <Button onclick={callback} position={position}>
        {switchOn ? 'Off' : 'On'};
    </Button> 
};

export default LightSwitch;