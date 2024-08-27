import React from 'react'

// Configs
import {POSTER_SIZE, BACKDROP_SIZE, IMAGE_BASE_URL} from '../../config'

// Components

// Hooks
import { useState } from 'react';
import { useEffect } from 'react';

// Images

import NoImage from '..//../images/no_image.jpg'

const Home = () => {
    const [state, setState] = useState();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    return (
        <>
            <div>
                <h2>This is Home Page.</h2>
            </div>
        </>
    )
};

export default Home;