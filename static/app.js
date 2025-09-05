document.getElementById("tokenizeBtn").addEventListener("click", async () => {
    const text = document.getElementById("textInput").value;
    const method = document.getElementById("methodSelect").value;
  
    const response = await axios.post("/tokenize", { text, method });
    const data = response.data;
  
    // --- Tokens Tab ---
    const tokensDiv = document.getElementById("tokensOutput");
    tokensDiv.innerHTML = "";
    data.tokens.forEach((tok, i) => {
      const span = document.createElement("span");
      span.className = "token";
      span.style.backgroundColor = randomColor(i);
      span.innerText = tok;
      tokensDiv.appendChild(span);
    });
  
    // --- One-Hot Encoding Tab (word-level only) ---
    const oneHotDiv = document.getElementById("oneHotOutput");
    let table = `<table class="table table-bordered table-sm"><thead><tr><th>Word</th>`;
    data.vocab.forEach(v => { table += `<th>${v}</th>`; });
    table += `</tr></thead><tbody>`;
    data.one_hot_words.forEach((word, i) => {
      table += `<tr><td>${word}</td>`;
      data.one_hot[i].forEach(val => {
        table += `<td>${val}</td>`;
      });
      table += `</tr>`;
    });
    table += `</tbody></table>`;
    oneHotDiv.innerHTML = table;

      // --- Metrics ---
const metricsDiv = document.getElementById("metricsOutput");
metricsDiv.innerHTML = `
  <ul class="list-group list-group-horizontal">
    <li class="list-group-item">Tokens: ${data.metrics.num_tokens}</li>
    <li class="list-group-item">Words: ${data.metrics.num_words}</li>
    <li class="list-group-item">Avg. Token Length: ${data.metrics.avg_token_len}</li>
    <li class="list-group-item">Fertility Ratio: ${data.metrics.fertility_ratio}</li>
  </ul>
`;
  });



  
  function randomColor(i) {
    const colors = ["#e0f7fa", "#f1f8e9", "#fff3e0", "#fce4ec", "#e8eaf6", "#f3e5f5"];
    return colors[i % colors.length];
  }
  