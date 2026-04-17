// API functions for the book AI frontend
import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

export const getBooks = () => API.get("/books/");
export const getRecommendations = (id) =>
  API.get(`/recommend/${id}/`);
export const askQuestion = (question) =>
  API.post("/ask/", { question });
export const fetchBooks = (query, max_results) =>
  API.post("/fetch-books/", { query, max_results });