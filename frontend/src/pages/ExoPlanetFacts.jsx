import React, { useState, useEffect } from 'react';
import "../assets/styles/ExoPlanetFacts.css"
import BlackBox from '../components/BlackBox';
import ZoomablePlanet from '../components/ZoomablePlanet';
const mockExoplanetData = {
    name: 'Kepler-452b',
    distanceFromEarth: 1400, // in light-years
    orbitTime: 385, // in days
    mass: 5, // times Earth's mass
    radius: 1.5, // times Earth's radius
    temperature: 265, // in Kelvin
  };
const FactsPage = () => {
  const [exoplanetData, setExoplanetData] = useState(null);

  // Function to fetch data from the API
  const fetchExoplanetData = async () => {
    try {
    //   const response = await fetch('API_URL_HERE'); // Replace with actual API URL
    //   const data = await response.json();
      setExoplanetData(mockExoplanetData); //Change to data
    } catch (error) {
      console.error('Error fetching exoplanet data:', error);
    }
  };

  useEffect(() => {
    fetchExoplanetData();
  }, []);

  if (!exoplanetData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="FactsPageContainer">
      {exoplanetData && (
        <BlackBox
          title={exoplanetData.name}
          planetname={exoplanetData.distanceFromEarth}
          maintext={exoplanetData.orbitTime}
        />
      )}
      {exoplanetData && (
        <div className="planet-corners">
        <ZoomablePlanet
          planetName={exoplanetData.name}
          facts={`Distance from Earth: ${exoplanetData.distanceFromEarth} light-years, Mass: ${exoplanetData.mass} times Earth's mass`}
        />
        <ZoomablePlanet
          planetName={exoplanetData.name}
          facts={`Radius: ${exoplanetData.radius} times Earth's radius, Temperature: ${exoplanetData.temperature} K`}
        />
        <ZoomablePlanet
          planetName={exoplanetData.name}
          facts={`Orbit Time: ${exoplanetData.orbitTime} days`}
        />
        <ZoomablePlanet
          planetName={exoplanetData.name}
          facts={`Distance from Earth: ${exoplanetData.distanceFromEarth} light-years, Mass: ${exoplanetData.mass} times Earth's mass`}
        />
      </div>
      )}
    </div>
  );
};

export default FactsPage;
