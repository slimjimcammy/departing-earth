import React, { useState } from 'react';
import '../assets/styles/Home.css';
import BlackBox from '../components/BlackBox';
import ExploreExoPlanet from '../components/ExploreExoPlanet';


const Home = () => {

    return (
        <body>
            <div className='BlurredImage'></div>
            <div className='HomePage'>
                <BlackBox title="WELCOME TO" planetname="EARTH"
                    maintext="SUCKIN CRAZY ON BLACK STROKES" />
            </div>
        </body>
    );
};

export default Home;