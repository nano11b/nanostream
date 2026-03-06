import os
import random
import subprocess
import redis
from server.config import MUSIC_ROOT, ICECAST_HOST, ICECAST_PORT, ICECAST_PASSWORD, REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def play(song,mount):

    url = f"icecast://source:{ICECAST_PASSWORD}@{ICECAST_HOST}:{ICECAST_PORT}/{mount}"

    cmd = [
        "ffmpeg",
        "-re",
        "-i",song,
        "-vn",
        "-c:a","libmp3lame",
        "-b:a","192k",
        "-f","mp3",
        url
    ]

    subprocess.run(cmd)

def start_station(name,cfg):

    folder = os.path.join(MUSIC_ROOT,cfg["playlist"])

    while True:

        request = r.lpop("song_requests")

        if request and os.path.exists(request):
            song = request
        else:
            songs = [s for s in os.listdir(folder) if s.endswith(".mp3")]
            if not songs:
                continue
            song = os.path.join(folder,random.choice(songs))

        print("Now playing:",song)
        play(song,cfg["mount"])