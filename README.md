# Python Radio Server v2

Features
- Multiple radio stations
- Auto DJ streaming via FFmpeg + Icecast
- Spotify-style web UI
- Discord song request queue
- Redis request queue
- Listener analytics endpoint

Requirements
- Python 3.10+
- ffmpeg
- icecast2
- redis-server

Install dependencies:

pip install fastapi uvicorn redis requests discord.py python-multipart

Run services:

redis-server
uvicorn server.main:app --host 0.0.0.0 --port 9000

Open UI:
http://localhost:9000