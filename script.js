fetch("data/games.json")
  .then(res => res.json())
  .then(games => {
    const fuse = new Fuse(games, {
      keys: ["title"],
      threshold: 0.4
    });

    const searchBox = document.getElementById("searchBox");
    const resultsDiv = document.getElementById("results");

    searchBox.addEventListener("input", e => {
      const query = e.target.value;
      const results = fuse.search(query);

      resultsDiv.innerHTML = results.map(r =>
        `<div><a href="${r.item.url}" target="_blank">${r.item.title}</a></div>`
      ).join("");
    });
  });
