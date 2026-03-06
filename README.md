# NanoStream PRSS (Python Radio Streaming Server)

Features:
- Multiple radio stations
- Auto DJ playlists
- Icecast streaming via FFmpeg
- FastAPI dashboard
- Discord song request bot (basic example)
- Listener analytics endpoint

Requirements:
- Python 3.10+
- ffmpeg
- icecast2

Install Python deps:

pip install fastapi uvicorn sqlalchemy python-socketio aiofiles discord.py mutagen redis requests

Run:

uvicorn server.main:app --host 0.0.0.0 --port 9000

Icecast default stream example:
http://localhost:8000/lofi