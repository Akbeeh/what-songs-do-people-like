import { Button } from "primereact/button";
import { Link } from "react-router-dom";
import "../App.css";
import { TopBar } from "../components/TopBar";

function Home() {
  return (
    <>
      <TopBar />
      <h1>What songs do people like?</h1>
      <div className="card">
        <Button
          label="My Profile"
          icon="pi pi-user"
          className="mr-3"
          aria-label="Profile"
        />
        <Link to="/top-songs">
          <Button
            label="Top Songs"
            icon="pi pi-flag-fill"
            aria-label="Top Songs"
          />
        </Link>
      </div>
    </>
  );
}

export default Home;
