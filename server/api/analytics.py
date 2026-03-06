import requests

ICECAST_STATS_URL = "http://localhost:8000/status-json.xsl"

def get_listener_count():

    try:
        data = requests.get(ICECAST_STATS_URL).json()

        sources = data["icestats"]["source"]

        if isinstance(sources, list):
            return sum(s["listeners"] for s in sources)

        return sources["listeners"]

    except:
        return 0