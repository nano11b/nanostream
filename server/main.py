from fastapi import FastAPI
from server.radio.station_manager import start_all_stations

app = FastAPI(title="Python Radio Server")

@app.on_event("startup")
def startup():
    start_all_stations()

@app.get("/stations")
def stations():
    return [
        {"name":"LoFi","mount":"lofi"},
        {"name":"Rock","mount":"rock"}
    ]