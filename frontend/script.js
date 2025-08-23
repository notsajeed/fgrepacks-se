const searchBox = document.getElementById("searchBox");
const resultsDiv = document.getElementById("results");

// Query Meilisearch
async function searchGames(query) {
  if (!query) return [];

  const res = await fetch("http://127.0.0.1:7700/indexes/games/search", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ q: query })
  });

  const data = await res.json();
  return data.hits;
}

searchBox.addEventListener("input", async (e) => {
  const query = e.target.value.trim();
  resultsDiv.innerHTML = "";

  if (!query) return;

  const hits = await searchGames(query);
  console.log(hits);

  if (!hits.length) {
    resultsDiv.innerHTML = `<div>No results found.</div>`;
    return;
  }

  resultsDiv.innerHTML = hits.map(hit =>
    `<div><a href="${hit.url}" target="_blank">${hit.title}</a></div>`
  ).join("");
});
