
# FitGirl Repacks Search Engine

A modern, fast, and user-friendly search engine for **FitGirl Repack** games using **Meilisearch** and a web frontend. Users can search for games by full title or common abbreviations (e.g., `NFS` → *Need for Speed*, `GTA` → *Grand Theft Auto*).

---

## Features

- 🔍 **Fuzzy Search** with support for common game abbreviations  
- 💻 **Minimal, modern dark-themed frontend**  
- ⚡ **Powered by Meilisearch** for fast search results  
- 📦 **Handles thousands of game entries efficiently**  
- 🔗 **Redirects users directly** to the original FitGirl Repack game page  

---

## Tech Stack

- **Backend:** Python + Meilisearch  
- **Frontend:** HTML, CSS, JavaScript  
- **Search Library:** Meilisearch  

---

## Installation

### 1. Install Meilisearch

Download the Meilisearch binary for Windows and run:

```bash
meilisearch.exe --http-addr 127.0.0.1:7700
````

### 2. Install Python Dependencies

```bash
pip install meilisearch requests beautifulsoup4
```

### 3. Clone the Repository

```bash
git clone https://github.com/notsajeed/fgrepacks-se
cd fgrepacks
```

### 4. Prepare Data

Make sure the `data/` folder contains your `games.json` or `games_with_aliases.json`.

---

## Backend Scripts

| Script              | Description                                                                    |
| ------------------- | ------------------------------------------------------------------------------ |
| `scrape_fitgirl.py` | Scrapes FitGirl Repack pages and saves to `games.json`.                        |
| `makealias.py`      | Adds common abbreviations to your games and creates `games_with_aliases.json`. |
| `index_games.py`    | Indexes games into Meilisearch for search functionality.                       |

---

## Frontend

| File                  | Description                            |
| --------------------- | -------------------------------------- |
| `frontend/index.html` | Main page                              |
| `frontend/style.css`  | Styles for the search page             |
| `frontend/script.js`  | Handles search requests to Meilisearch |

Open `index.html` in your browser, type a game title or abbreviation, and see results in real-time.

---

## Folder Structure

```
fitgirl-search/
│
├── backend/
│   ├── index_games.py
│   ├── makealias.py
│   └── scrape_fitgirl.py
│
├── data/
│   ├── games.json
│   └── games_with_aliases.json
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Usage

1. Start Meilisearch:

```bash
meilisearch.exe --http-addr 127.0.0.1:7700
```

2. Scrape new games (optional):

```bash
python backend/scrape_fitgirl.py
```

3. Generate aliases:

```bash
python backend/makealias.py
```

4. Index games in Meilisearch:

```bash
python backend/index_games.py
```

5. Open the frontend:

Open `frontend/index.html` in your browser.

---

## Tips

* Add more aliases in `makealias.py` to improve search results
* Keep `games.json` updated with the latest FitGirl Repack releases
* Adjust Meilisearch settings like `searchableAttributes` and `rankingRules` for better ranking

---

## License

**MIT License** – free to use, modify, and distribute

---

## Acknowledgements

* **[FitGirl Repacks](https://fitgirl-repacks.site/)** – Source of game data
* **[Meilisearch](https://www.meilisearch.com/)** – Powerful search engine
* **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** – Web scraping library
