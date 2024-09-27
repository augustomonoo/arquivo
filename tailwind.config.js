/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./arquivo/templates/**/*.html", "./arquivo/static/**/*.js", "./arquivo/**/*/.py"],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/forms"),
  ],
}
