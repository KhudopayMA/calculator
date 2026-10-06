document.getElementById("calc").addEventListener("click", async () => {
  const out = document.getElementById("result");
  const a = document.getElementById("a").value.trim();
  const op = document.getElementById("op").value;
  const b = document.getElementById("b").value.trim();

  const response = await fetch("/api/calculate", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({a, op, b})
  });
  const data = await response.json();

  out.className = response.ok ? "" : "error";
  out.textContent = response.ok ? `${a} ${op} ${b} = ${data}` : data.error;
});
