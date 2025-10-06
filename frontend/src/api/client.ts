import axios from "axios";

const apiBaseFromEnv = (import.meta as any).env?.VITE_API_BASE;
const defaultBase =
  typeof window !== "undefined"
    ? `${window.location.origin}/api/v1`
    : "/api/v1";
const baseURL = apiBaseFromEnv || defaultBase;

export const api = axios.create({
  baseURL,
  timeout: 10000,
  headers: { "Content-Type": "application/json" },
});

export function setToken(token?: string) {
  if (token) api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  else delete api.defaults.headers.common["Authorization"];
}

export default api;
