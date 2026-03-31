const APP_PARTS = [
  "./app.part1.txt",
  "./app.part2.txt",
  "./app.part3.txt",
  "./app.part4.txt",
  "./app.part5.txt",
  "./app.part6.txt",
];

function decodeEscapedChunk(chunk) {
  return JSON.parse(`"${chunk}"`);
}

async function loadApp() {
  const responses = await Promise.all(APP_PARTS.map((path) => fetch(path)));
  responses.forEach((response) => {
    if (!response.ok) {
      throw new Error(`Failed to load ${response.url}`);
    }
  });

  const escapedParts = await Promise.all(responses.map((response) => response.text()));
  const source = escapedParts.map(decodeEscapedChunk).join("");
  const script = document.createElement("script");
  script.text = source;
  document.body.appendChild(script);
}

loadApp().catch((error) => {
  console.error(error);
  document.body.insertAdjacentHTML(
    "beforeend",
    '<div style="position:fixed;right:16px;bottom:16px;padding:12px 14px;border-radius:12px;background:#ff6c78;color:#fff;z-index:9999;font-family:Segoe UI,sans-serif;">Не удалось загрузить клиентскую логику</div>',
  );
});
