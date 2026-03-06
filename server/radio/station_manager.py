import threading
from server.radio.auto_dj import start_station

STATIONS = {
    "lofi": {
        "mount":"lofi",
        "playlist":"lofi"
    },
    "rock": {
        "mount":"rock",
        "playlist":"rock"
    }
}

def start_all_stations():
    for name, cfg in STATIONS.items():
        t = threading.Thread(target=start_station, args=(name,cfg))
        t.daemon = True
        t.start()