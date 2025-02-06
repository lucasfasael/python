import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { Dancing_Script } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// Adicionando a fonte Dancing Script
const dancingScript = Dancing_Script({
  weight: ["400", "700"], // Defina os pesos que você quer usar (sem o `..` aqui)
  subsets: ["latin"],
  variable: "--font-dancing-script", // Define uma variável CSS para usar na classe
});

export const metadata: Metadata = {
  title: "Text Hunter 🏹",
  description: "Um caçador de textos !",
  icons:{
    icon: {
      url: "/iaGirl.jpeg",
      
    }
  }
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-br">
      <body
  className={`${geistSans.variable} ${geistMono.variable} ${dancingScript.variable} 
              relative 
              before:content-[''] before:absolute before:inset-0 before:bg-black/30 before:-z-10
              antialiased`}
>
        {children}
      </body>
    </html>
  );
}
