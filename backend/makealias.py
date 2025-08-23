import json

with open("../data/games.json", "r", encoding="utf-8") as f:
    games = json.load(f)

abbr_map = {
    "Call of Duty": ["cod"],
    "Grand Theft Auto": ["gta"],
    "Need for Speed": ["nfs"],
    "Far Cry": ["farcry"],
    "Assassin's Creed": ["ac"],
    "The Elder Scrolls": ["tes"],
    "Final Fantasy": ["ff"],
    "The Witcher": ["tw"],
    "Halo": ["halo"],
    "Minecraft": ["mc"],
    "Red Dead Redemption": ["rdr"],
    "Battlefield": ["bf"],
    "Resident Evil": ["re"],
    "Metal Gear Solid": ["mgs"],
    "Uncharted": ["uc"],
    "Tomb Raider": ["tr"],
    "Dark Souls": ["ds"],
    "Bloodborne": ["bb"],
    "Overwatch": ["ow"],
    "League of Legends": ["lol"],
    "World of Warcraft": ["wow"],
    "StarCraft": ["sc"],
    "Diablo": ["diablo"],
    "The Sims": ["sims"],
    "Pokémon": ["poke"],
    "Zelda": ["zelda"],
    "Super Mario": ["sm"],
    "Donkey Kong": ["dk"],
    "Metroid": ["metroid"],
    "Kirby": ["kirby"],
    "Splatoon": ["splatoon"],
    "Xenoblade Chronicles": ["xenoblade"],
    "Persona": ["persona"],
    "Yakuza": ["yakuza"],
    "Bayonetta": ["bayonetta"],
    "Hollow Knight": ["hk"],
    "Celeste": ["celeste"],
    "Cuphead": ["cuphead"],
    "Hades": ["hades"],
    "Stardew Valley": ["stardew"],
    "Horizon Zero Dawn": ["hzd"],
    "God of War": ["gow"],
    "Spider-Man": ["spiderman"],
    "The Last of Us": ["tlou"],
    "Ghost of Tsushima": ["ghost tsushima"],
    "Sekiro": ["sekiro"],
    "Nioh": ["nioh"],
    "Monster Hunter": ["mh"],
    "Dragon Age": ["da"],
    "Mass Effect": ["me"],
    "Fallout": ["fallout"],
    "Doom": ["doom"],
    "Quake": ["quake"],
    "Wolfenstein": ["wolfenstein"],
    "Left 4 Dead": ["l4d"],
    "Dead Space": ["dead space"],
    "Silent Hill": ["sh"],
    "Outlast": ["outlast"],
    "Amnesia": ["amnesia"],
    "Until Dawn": ["until dawn"],
    "Heavy Rain": ["heavy rain"],
    "Detroit: Become Human": ["detroit"],
    "Tales of": ["tales"],
    "Ni no Kuni": ["nnk"],
    "Fire Emblem": ["fe"],
    "Advance Wars": ["aw"],
    "Kingdom Hearts": ["kh"]
}
for game in games:
    game_title = game["title"].lower()
    game["aliases"] = []

    for full_name, aliases in abbr_map.items():
        if full_name.lower() in game_title:
            game["aliases"].extend(aliases)

with open("../data/games_with_aliases.json", "w", encoding="utf-8") as f:
    json.dump(games, f, indent=2, ensure_ascii=False)

print("✅ Aliases added and saved as 'games_with_aliases.json'.")
