import yt_dlp
from termcolor import colored

def read_music_file(path):
    try:
        with open(path, "r") as file:
            return file.readlines()
    except Exception as e:
        print(colored(f"Error reading file {path}: {e}", "red"))
        return []

def main():
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
        }],
        'outtmpl': 'songs/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        songs = read_music_file("songs.txt")
        for i, song in enumerate(songs):
            try:
                print(colored(f"\n------------------------------------  Downloading song number {i+1}  -------------------------------------\n", "green"))
                ydl.download([song.strip()])
                print(colored("\n---------------------------------------------  Done  -------------------------------------------------\n", "green"))
            except Exception as e:
                print(colored(f"Error downloading song number {i+1}: {e}", "red"))

if __name__ == "__main__":
    main()