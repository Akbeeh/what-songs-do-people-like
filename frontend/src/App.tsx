import { PrimeReactProvider } from "primereact/api";
import { Route, Routes } from "react-router-dom";
import About from "./pages/About.tsx";
import Home from "./pages/Home.tsx";
import Map from "./pages/Map.tsx";
import TopSongs from "./pages/TopSongs.tsx";

function App() {
  return (
    <PrimeReactProvider>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/map" element={<Map />} />
        <Route path="/top-songs" element={<TopSongs />} />
      </Routes>
    </PrimeReactProvider>
  );
}

export default App;
