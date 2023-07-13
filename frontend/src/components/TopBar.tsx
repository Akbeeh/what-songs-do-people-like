import GraphicEqIcon from "@mui/icons-material/GraphicEq";
import { Button } from "primereact/button";
import { Toolbar } from "primereact/toolbar";
import React from "react";
import { Link } from "react-router-dom";

export const TopBar = () => {
  const leftContents = (
    <React.Fragment>
      <Link to="/" style={{ display: "flex", alignItems: "center" }}>
        <GraphicEqIcon fontSize="large" />
        <span>What songs do people like?</span>
      </Link>
    </React.Fragment>
  );

  const rightContents = (
    <React.Fragment>
      <Link to="/about">
        <Button
          icon="pi pi-question-circle"
          className="mr-1"
          aria-label="About"
        />
      </Link>
      <Link to="/top-songs">
        <Button icon="pi pi-map" className="mr-1" aria-label="Map" />
      </Link>
      <Button icon="pi pi-language" className="mr-1" aria-label="Language" />
      <Button icon="pi pi-sun" aria-label="Theme" />
    </React.Fragment>
  );

  return (
    <>
      <Toolbar start={leftContents} end={rightContents} />
    </>
  );
};
