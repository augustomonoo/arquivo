/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./arquivo/templates/**/*.html", "./arquivo/static/**/*.js", "./arquivo/**/*/.py"],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/forms"),
  ],
}
