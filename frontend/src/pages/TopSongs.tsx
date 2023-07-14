import { useEffect, useState } from "react";
import "../App.css";
import { TopBar } from "../components/TopBar";

function TopSongs() {
  const [topSongs, setTopSongs] = useState([]);

  useEffect(() => {
    const fetchTopSongs = async () => {
      try {
        const response = await fetch("/api/songs");
        const data = await response.json();
        setTopSongs(data);
      } catch (error) {
        console.error("Error fetching top songs:", error);
      }
    };

    fetchTopSongs();
  }, []);

  return (
    <>
      <TopBar />
      <div>
        <h1>Top 50 Songs</h1>
        <ul>
          {topSongs.map((song) => (
            <li key={song.id}>{song.title}</li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default TopSongs;
