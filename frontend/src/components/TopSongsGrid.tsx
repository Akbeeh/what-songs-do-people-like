import AlbumIcon from "@mui/icons-material/Album";

function TopSongsGrid({ song }) {
  const truncateText = (text, maxLength) => {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + "...";
    }
    return text;
  };

  return (
    <div className="col-12 sm:col-6 lg:col-12 xl:col-4 p-2">
      <div className="p-4 border-1 surface-border surface-card border-round">
        <div className="flex flex-column align-items-center gap-3 py-5">
          <img className="w-9 sm:w-16rem xl:w-10rem h-auto shadow-2 block xl:block mx-auto border-round"
            src={song.image}
            alt={song.title}
          />
          <span className="text-2xl font-bold">
              {truncateText(song.title, 30)}
          </span>
          <span className="flex align-items-center gap-2">
            <i className="pi pi-user"></i>
            <span className="font-semibold">
              {truncateText(song.artist, 20)}
            </span>
          </span>
          <span className="flex align-items-center gap-2">
            <AlbumIcon fontSize="medium" />
            <span className="font-semibold">
              {truncateText(song.album, 40)}
            </span>
          </span>
        </div>
        <div className="flex align-items-center justify-content-between">
          <span className="font-semibold">
            Released on {song.release_date}
          </span>
          <span className="font-semibold">{song.duration}</span>
        </div>
      </div>
    </div>
  );
}

export default TopSongsGrid;
