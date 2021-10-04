# Overview

A Prometheus exporter that spits out playtime information for a steam user.

Example:

```
# HELP steam_game_playtime_forever_seconds A games playtime from all time in seconds.
# TYPE steam_game_playtime_forever_seconds gauge
steam_game_playtime_forever_seconds{app_id="10",name="Counter-Strike",steam_id="76561197987123908"} 0.0
steam_game_playtime_forever_seconds{app_id="220",name="Half-Life 2",steam_id="76561197987123908"} 21720.0
steam_game_playtime_forever_seconds{app_id="240",name="Counter-Strike: Source",steam_id="76561197987123908"} 8220.0
steam_game_playtime_forever_seconds{app_id="380",name="Half-Life 2: Episode One",steam_id="76561197987123908"} 660.0
steam_game_playtime_forever_seconds{app_id="420",name="Half-Life 2: Episode Two",steam_id="76561197987123908"} 24720.0
steam_game_playtime_forever_seconds{app_id="17470",name="Dead Space",steam_id="76561197987123908"} 4920.0
steam_game_playtime_forever_seconds{app_id="3590",name="Plants vs. Zombies: Game of the Year",steam_id="76561197987123908"} 92220.0
```

# Setup

## Environment Variables:

### STEAM_KEY

To get a steam key, sign up for one here:
https://steamcommunity.com/dev

### STEAM_USER

To get your Steam User ID. Login and go to "view profile".
It should be in the URL bar where xxxxxx is:
`https://steamcommunity.com/profiles/xxxxxx`

### STEAM_SLEEP

Time in seconds between polling.
Defauls to 300

### STEAM_PORT

Port to launch server on.
Defaults to 8000

# Run

Build:
`docker build -t 'steam-exporter' .`

Run with Docker:
`docker run -e STEAM_KEY=$YOURSTEAMKEYHERE -e STEAM_USER=$YOURSTEAMUSERID  -p8000:8000  -it steam-exporter`

