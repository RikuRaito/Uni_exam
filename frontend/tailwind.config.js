/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",   // ← React (Vite) の場合これを追加
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}