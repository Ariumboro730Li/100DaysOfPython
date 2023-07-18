from yt_dlp import YoutubeDL

print("Welcome to Youtube Downloader")
print("\n\n")

while(True):
    URLS = input("Insert Youtube Link : (Use comma (,) to multiple links) ")
    output_dir = input("Enter the output directory: ")
    URL_LISTS = URLS.split((", "))

    output_path = f'/Users/ariumboroseno/Documents/100JutaPerbulan/professional_programmer/100DaysOfPython/youtube/{output_dir}/%(title)s.%(ext)s'

    ydl_opts = {
        'outtmpl': output_path,
        'ignoreerrors': True,
        'playliststart': 1,  # Specify the starting index of the playlist (default: 1)
        'playlistend': None,
    }

    try:
        for url in URL_LISTS:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url.strip()])
    except Exception as e:
        print(f"An error occured : {e}")
            