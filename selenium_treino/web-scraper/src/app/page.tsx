"use client";

import { useState } from "react";
import VideoButton from "./components/spellCaster";
import Image from "next/image";
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
    <div className="mx-auto flex h-full w-full flex-col items-center justify-center p-6">
      <div className="flex mt-10">
        <h1 className="font-dancing text-stroke-2 text-6xl font-bold text-customOrange">
          Text Hunter
        </h1>
        <Image
          src="/archer.webp" 
          alt="Descrição da imagem"
          width={160}
          height={200}
          className="-ml-36 top-1 absolute object-contain"
        />
      </div>
      <input
        className="mb-2 w-80 border p-2 z-20"
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Digite a URL da página . . ."
      />
      <button
        className={`mb-3 flex items-center justify-center px-4 py-2 ${
          loading
            ? "bg-blue-500"
            : text && text !== "Erro ao extrair texto. Verifique a URL."
              ? "bg-green-500"
              : "bg-blue-500"
        }`}
        onClick={fetchText}
        disabled={loading}
      >
        {loading ? (
          <>
            <svg
              className="mr-2 h-5 w-5 animate-spin text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8v8H4z"
              ></path>
            </svg>
            Extraindo...
          </>
        ) : (
          "Extrair Texto"
        )}
      </button>

      <pre className="text-stroke-1 w-100 hide-scrollbar h-full overflow-scroll text-wrap font-mono text-3xl font-bold text-white">
        {text}
      </pre>
      <VideoButton></VideoButton>
    </div>
  );
}
