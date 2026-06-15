/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        servimex: {
          blue: '#004d99',
          dark: '#003366',
          light: '#3385ff',
          navy: '#0A192F',
          accent: '#f1c40f',
          surface: '#F8FAFC'
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        heading: ['Outfit', 'sans-serif'],
      },
      animation: {
        'slow-spin': 'spin 4s linear infinite',
        'glow-pulse': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float-wave': 'float-wave 3.5s ease-in-out infinite',
      },
      keyframes: {
        'float-wave': {
          '0%, 100%': { transform: 'translateY(0px) rotate(0deg)' },
          '50%': { transform: 'translateY(-4px) rotate(1.5deg)' },
        }
      }
    }
  },
  plugins: [],
}
