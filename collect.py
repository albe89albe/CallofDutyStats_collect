import json, asyncio, callofduty
from callofduty import Mode, Platform, Title
from pathlib import Path

with open('config.json','r') as f:
    config = json.load(f)

async def getPlayerStats(playerTag, title = Title.ModernWarfare, mode = Mode.Warzone):
    client = await callofduty.Login(config['user'], config['pass'])

    results = await client.SearchPlayers(Platform.Activision, playerTag, limit=3)

    player = results[0]
    profile = await player.profile(title, mode)

    with open('out/'+playerTag+'.json','w') as f:
        f.write(json.dumps(profile))

players = config['playerTags']

Path('out').mkdir(parents=True, exist_ok=True)

for player in players:
    asyncio.get_event_loop().run_until_complete(getPlayerStats(player))