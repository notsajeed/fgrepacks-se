import meilisearch
import json
import os

DATA_FILE = "../data/games_with_aliases.json"
with open(DATA_FILE, encoding="utf-8") as f:
    games = json.load(f)

for i, game in enumerate(games):
    if 'id' not in game:
        game['id'] = i + 1

print(f"Loaded {len(games)} games.")

client = meilisearch.Client("http://127.0.0.1:7700")

try:
    index = client.get_index("games")
    print("Index exists, clearing old documents...")
    index.delete_all_documents()
except meilisearch.errors.MeiliSearchApiError:
    index = client.create_index("games", {'primaryKey': 'id'})
    print("Created new index with primary key 'id'.")

index.update_searchable_attributes(["title"])
index.update_searchable_attributes(["title", "aliases"])

task = index.add_documents(games)
client.wait_for_task(task.task_uid)

docs = index.get_documents().results[:5]
print("Sample documents:", docs)
