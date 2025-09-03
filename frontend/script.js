const searchBox = document.getElementById("searchBox");
const resultsDiv = document.getElementById("results");

const API_URL = "https://fgrepacks.onrender.com";

async function searchGames(query) {
  if (!query) return [];

  try {
    const res = await fetch(`${API_URL}/api/find/${encodeURIComponent(query)}`);
    if (!res.ok) throw new Error("Network error");
    const data = await res.json();
    return data.results || [];
  } catch (err) {
    console.error("Error fetching game:", err);
    return [];
  }
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
