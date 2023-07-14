import { useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import "../App.css";
import { TopBar } from "../components/TopBar";

const geoUrl =
  "https://raw.githubusercontent.com/deldersveld/topojson/master/world-countries.json";

function Map() {
  const [hoveredCountry, setHoveredCountry] = useState(null);

  const handleMouseEnter = (geo) => {
    setHoveredCountry(geo.properties.name);
  };

  const handleMouseLeave = () => {
    setHoveredCountry(null);
  };

  return (
    <>
      <TopBar />
      <div>
        <h1>Map</h1>
        <ComposableMap
          projection="geoMercator"
          projectionConfig={{ scale: 100 }}
        >
          <Geographies geography={geoUrl}>
            {({ geographies }) =>
              geographies.map((geo) => (
                <Geography
                  key={geo.rsmKey}
                  geography={geo}
                  fill={
                    geo.properties.name === hoveredCountry ? "blue" : "#ccc"
                  }
                  onMouseEnter={() => handleMouseEnter(geo)}
                  onMouseLeave={handleMouseLeave}
                  onClick={() => {}}
                />
              ))
            }
          </Geographies>
        </ComposableMap>
      </div>
    </>
  );
}

export default Map;
