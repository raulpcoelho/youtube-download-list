import yt_dlp
from termcolor import colored

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
        songs = read_music_file("songs.txt")
        for i, song in enumerate(songs):
            print(colored(f"\n------------------------------------  Downloading song number {i+1}  -------------------------------------\n", "green"))
            ydl.download(song)
            print(colored("\n---------------------------------------------  Done  -------------------------------------------------\n", "green"))

if __name__ == "__main__":
    main()

