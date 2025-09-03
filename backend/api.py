from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fgrepacks-se.vercel.app"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "games_with_aliases.json")

with open(DATA_FILE, encoding="utf-8") as f:
    games = json.load(f)


@app.get("/api/find/{query}")
def find_game(query: str):
    q = query.strip().lower()
    results = []

    for game in games:
        title = game["title"].lower()

        if q in title:
            results.append(game)
            continue

        if "aliases" in game and any(q in alias.lower() for alias in game["aliases"]):
            results.append(game)

    return {"results": results[:10]}  
