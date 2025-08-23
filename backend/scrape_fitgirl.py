import requests
from bs4 import BeautifulSoup
import json
import time
import os
import random

BASE_URL = "https://fitgirl-repacks.site/page/{}/"

games = []

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/127.0.0.1 Safari/537.36"
}

SAVE_PATH = "data/games.json"

def get_last_page():
    r = requests.get(BASE_URL.format(1), headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    page_links = soup.select("a.page-numbers")
    if not page_links:
        return 1
    try:
        last_page = max(int(link.text) for link in page_links if link.text.isdigit())
        return last_page
    except:
        return 1

def scrape_page(page_num):
    url = BASE_URL.format(page_num)
    print(f"\n📥 Fetching page {page_num}: {url}")

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"⚠️ Failed at page {page_num}: {e}")
        return False

    soup = BeautifulSoup(r.text, "html.parser")
    posts = soup.select("h1.entry-title a")

    if not posts:
        return False

    before = len(games)
    for post in posts:
        entry = {
            "title": post.text.strip(),
            "url": post["href"]
        }
        if entry not in games:
            games.append(entry)

    after = len(games)
    print(f"✅ Added {after - before} games. Total so far: {after}")
    return True

def save_progress():
    os.makedirs("data", exist_ok=True)
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(games, f, indent=2, ensure_ascii=False)
    print(f"💾 Progress saved ({len(games)} games).")

def main():
    start_page = 1
    if os.path.exists(SAVE_PATH):
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            try:
                saved = json.load(f)
                games.extend(saved)
                print(f"🔄 Resuming with {len(games)} already saved games...")
                start_page = (len(games) // 10) + 1  # next page
            except:
                print("⚠️ Could not load old data. Starting fresh.")

    last_page = get_last_page()
    print(f"🔎 Detected {last_page} pages of games.")

    for i in range(start_page, last_page + 1):
        if not scrape_page(i):
            print(f"⚠️ Stopped at page {i}")
            break

        time.sleep(random.uniform(1, 3))

        if i % 50 == 0:
            save_progress()

    save_progress()
    print(f"\n🎉 Done! Collected {len(games)} games!")

if __name__ == "__main__":
    main()
