/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {
      colors: {
        brand: {
          purple: "#115e59", // Dark teal matching "DUA"
          blue: "#84cc16", // Light green matching "LINK"
        },
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
        display: ['"Plus Jakarta Sans"', "sans-serif"],
      },
      backgroundImage: {
        "brand-gradient":
          "linear-gradient(135deg, #115e59 0%, #84cc16 100%)",
      },
      animation: {
        float: "float 6s ease-in-out infinite",
        "float-delayed": "float 6s ease-in-out infinite 3s",
        shine: "shine 2s linear infinite",
      },
      keyframes: {
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-20px)" },
        },
        shine: {
          to: { backgroundPosition: "200% center" },
        },
        progress: {
          "0%": { transform: "scaleX(0)" },
          "100%": { transform: "scaleX(1)" },
        },
      },
    },
  },
  plugins: [],
}
