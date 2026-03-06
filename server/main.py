from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from server.radio.station_manager import start_all_stations
import redis
from server.config import REDIS_HOST, REDIS_PORT

app = FastAPI()

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

app.mount("/static", StaticFiles(directory="web"), name="static")

@app.on_event("startup")
def start_radio():
    start_all_stations()

@app.get("/", response_class=HTMLResponse)
def index():
    with open("web/index.html") as f:
        return f.read()

@app.get("/api/stations")
def stations():
    return [
        {"name":"LoFi","mount":"lofi"},
        {"name":"Rock","mount":"rock"}
    ]

@app.get("/api/requests")
def requests():
    return list(r.lrange("song_requests",0,-1))