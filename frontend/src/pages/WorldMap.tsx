import "leaflet/dist/leaflet.css";
// import { SetStateAction, useState } from "react";
// import { GeoJSON, MapContainer, TileLayer } from "react-leaflet";
import "../App.css";
import { TopBar } from "../components/TopBar";

// const geoUrl =
//   "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson";

function WorldMap() {
  // const [hoveredCountry, setHoveredCountry] = useState(null);

  // const handleMouseEnter = (geo: {
  //   properties: { name: SetStateAction<null> };
  // }) => {
  //   setHoveredCountry(geo.properties.name);
  // };

  // const handleMouseLeave = () => {
  //   setHoveredCountry(null);
  // };

  // const countryStyle = (feature: { properties: { name: null } }) => ({
  //   fillColor: feature.properties.name === hoveredCountry ? "blue" : "#ccc",
  //   fillOpacity: 0.5,
  //   color: "white",
  //   weight: 2,
  //   dashArray: "3",
  // });

  return (
    <>
      <TopBar />
      <div>
        <h1>Map</h1>
        {/* <div className="card">
          <MapContainer
            className="world-map"
            center={[45, 0]}
            zoom={2}
            minZoom={2}
            maxZoom={2}
            style={{ height: "700px", width: "100%" }}
          >
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            <GeoJSON
            data={geoUrl}
            style={countryStyle}
            onEachFeature={(feature, layer) => {
              layer.on({
                mouseover: () => handleMouseEnter(feature),
                mouseout: handleMouseLeave,
              });
            }}
          />
          </MapContainer>
        </div> */}
      </div>
    </>
  );
}

export default WorldMap;
