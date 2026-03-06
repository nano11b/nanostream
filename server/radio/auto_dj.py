import subprocess
import os
import random
from server.config import ICECAST_HOST, ICECAST_PORT, ICECAST_SOURCE_PASSWORD, MUSIC_ROOT

def play_song(song, mount):

    url = f"icecast://source:{ICECAST_SOURCE_PASSWORD}@{ICECAST_HOST}:{ICECAST_PORT}/{mount}"

    cmd = [
        "ffmpeg",
        "-re",
        "-i", song,
        "-vn",
        "-c:a","libmp3lame",
        "-b:a","192k",
        "-f","mp3",
        url
    ]

    subprocess.run(cmd)


def start_station(name, cfg):

    playlist_dir = os.path.join(MUSIC_ROOT, cfg["playlist"])

    while True:

        songs = [s for s in os.listdir(playlist_dir) if s.endswith(".mp3")]

        if not songs:
            print(f"No songs found in {playlist_dir}")
            return

        song = random.choice(songs)
        path = os.path.join(playlist_dir, song)

        print(f"[{name}] Now playing:", song)

        play_song(path, cfg["mount"])