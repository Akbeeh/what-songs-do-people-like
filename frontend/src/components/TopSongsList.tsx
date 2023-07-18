import AlbumIcon from "@mui/icons-material/Album";

function TopSongsList({ song }) {
  const truncateText = (text, maxLength) => {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + "...";
    }
    return text;
  };

  return (
    <div className="col-12">
      <div className="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4">
        <div className="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
          <div className="flex flex-column align-items-center sm:align-items-start gap-3">
            <div className="text-2xl font-bold text-900">
              {truncateText(song.title, 30)}
            </div>
            <div className="flex align-items-center gap-3">
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
          </div>
          <div className="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-2 gap-4">
            <span className="font-semibold">{song.release_date}</span>
          </div>
          <div className="flex sm:flex-column align-items-center sm:align-items-end sm:gap-2">
            <span className="text-2xl font-semibold">{song.duration}</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TopSongsList;
