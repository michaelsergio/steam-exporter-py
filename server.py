from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import os
import requests

# Metric to track time spent and requests made.
REQUEST_TIME = Summary('steam_request_processing_seconds', 'Time spent processing request')

# Metric for the game playtime_forever
GAME_PLAYTIME_FOREVER = Gauge(
        'steam_game_playtime_forever_seconds', 
        'A games playtime from all time in seconds.',
        ["name", "app_id", "steam_id"])

DOMAIN = "https://api.steampowered.com"
OWNED_GAMES_ENDPOINT = "/IPlayerService/GetOwnedGames/v0001/"
STEAM_KEY = os.getenv('STEAM_KEY')
STEAM_USER = os.getenv('STEAM_USER')

PORT = int(os.getenv("STEAM_PORT", "8000"))
STEAM_SLEEP = int(os.getenv("STEAM_SLEEP", "300"))

@REQUEST_TIME.time()
def update_stats():
    print("Processing request")
    r = requests.get(
            DOMAIN + OWNED_GAMES_ENDPOINT,
            params = {
                "key": STEAM_KEY, 
                "steamid": STEAM_USER,
                "format":"json",
                "include_appinfo":"true",
                "include_played_free_games":"true"
                })

    print(f"Status: {r.status_code}")
    #print(r.url)

    game_count = r.json()['response']['game_count']
    print(f"Found {game_count} games")

    games = r.json()['response']['games']
    for game in games:
        id = game["appid"]
        name = game["name"]
        playtime_forever_min = game["playtime_forever"]
        # prometheus prefers seconds
        playtime_forever_sec  = playtime_forever_min *  60

        GAME_PLAYTIME_FOREVER.labels(
                name=name, 
                app_id=id, 
                steam_id=STEAM_USER
        ).set(playtime_forever_sec)

if __name__ == '__main__':
    start_http_server(PORT)
    print(f"Server running on {PORT}")
    while True:
        update_stats()
        time.sleep(STEAM_SLEEP)


