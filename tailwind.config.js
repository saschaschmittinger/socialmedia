// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/"], // updated line here!
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark"],
    darkTheme: "dark",
  },
  safelist: ["alert-info", "alert-success", "alert-warning", "alert-error"],
};
