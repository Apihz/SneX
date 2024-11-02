/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'norwester': ['Norwester', 'sans-serif'],  // Norwesters from CDN
        'satoshi': ['Satoshi', 'sans-serif'],         // Satoshi from Fontshare
        'bebas': ['Bebas Neue', 'sans-serif'],        // Bebas Neue from Fontshare
      },
      screens: {
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
        '3xl': '1720px',
      },
    },
  },
  plugins: [require('tailwindcss-primeui')],
}
