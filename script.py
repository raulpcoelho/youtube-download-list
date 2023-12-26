import yt_dlp

def read_music_file(path):
    with open(path, "r") as file:
        return file.readlines()

def main():
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],   
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(read_music_file("musicas.txt"))

if __name__ == "__main__":
    main()
