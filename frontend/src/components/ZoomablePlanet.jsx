import React, { useState } from 'react';
import '../assets/styles/ZoomablePlanet.css'; // Ensure you create a CSS file for styles

const ZoomablePlanet = ({ planetName, facts }) => {
  const [isZoomed, setIsZoomed] = useState(false);

  const handleClick = () => {
    setIsZoomed(true); // Show the fact box
  };

  const handleClose = () => {
    setIsZoomed(false); // Close the fact box
  };

  return (
    <div className="planet-container">
      <img
        src="./src/assets/images/Moon.svg" // Replace with your planet image URL
        alt={planetName}
        className="planet-image"
        onClick={handleClick}
      />
      {isZoomed && (
        <div className="fact-overlay">
          <div className="fact-box">
            <button className="close-button" onClick={handleClose}>✖</button>
            <h3>{planetName}</h3>
            <p>{facts}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default ZoomablePlanet;
