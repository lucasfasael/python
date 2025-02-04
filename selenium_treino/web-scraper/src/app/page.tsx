"use client";

import { useState } from "react";

export default function WebScraper() {
  const [url, setUrl] = useState("");
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchText = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:5000/extract", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        throw new Error("Erro ao buscar dados");
      }

      const data = await response.json();
      setText(data.text);
    } catch (error) {
      console.error(error);
      setText("Erro ao extrair texto. Verifique a URL.");
    }
    setLoading(false);
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Extrator de Texto Web</h1>
      <input
        className="border p-2 w-full mb-2"
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Digite a URL da página"
      />
      <button
        className="bg-blue-500 text-white px-4 py-2"
        onClick={fetchText}
        disabled={loading}
      >
        {loading ? "Extraindo..." : "Extrair Texto"}
      </button>
      <pre className="mt-4 p-2 border whitespace-pre-wrap">{text}</pre>
    </div>
  );
}
