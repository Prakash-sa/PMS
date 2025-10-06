import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  // use relative paths so the built `dist` can be served from any location
  // and module assets won't request absolute paths like `/assets/...` which
  // may return the SPA index.html and cause MIME type errors.
  base: "./",
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://localhost:80",
    },
  },
});
