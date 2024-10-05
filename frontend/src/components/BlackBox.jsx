import React, { useState } from 'react';
import '../assets/styles/BlackBox.css'
import ExploreExoPlanet from './ExploreExoPlanet';
const BlackBox = ({ title, planetname, maintext }) => {
    const [showExplore, setShowExplore] = useState(false);

    // This function toggles the visibility of the ExploreExoPlanet component
    const handleButtonClick = () => {
        setShowExplore(true);
    };
    return (
        <div className='BlackBoxMainContainer'>
            <h1>{title}</h1>
            <h2>{planetname}</h2>
            <p>{maintext}</p>
            <div className="ExploreButtonWrapper">
            <button className='ExploreButton' onClick={handleButtonClick}>
                Explore Exoplanet
            </button>
            {/* Conditionally render ExploreExoPlanet when the button is clicked */}
            {showExplore && <ExploreExoPlanet />}
            </div>
        </div>
    );
};

export default BlackBox;
