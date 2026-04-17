import { useEffect, useState } from "react";
import { getBooks, fetchBooks } from "../api/api";
import BookCard from "../components/BookCard";

function Home({ onSelectBook }) {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [fetching, setFetching] = useState(false);
  const [query, setQuery] = useState("");

  const loadBooks = () => {
    setLoading(true);
    getBooks()
      .then((res) => {
        setBooks(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  };

  useEffect(() => {
    loadBooks();
  }, []);

  const handleFetch = async () => {
  setFetching(true);

  try {
    const finalQuery = query.trim() || "harry potter";

    await fetchBooks(finalQuery, 5);
    await loadBooks();
  } catch (err) {
    console.error("Fetch error:", err);
  }

  setFetching(false);
  };

  return (
    <div>
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-6 gap-3">
  <h1 className="text-3xl font-bold">
    📚 Book Dashboard
  </h1>

      <div className="flex gap-2">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search books (e.g. Harry Potter)"
          className="p-2 rounded bg-gray-800 text-white"
        />

        <button
          onClick={handleFetch}
          className="bg-green-600 px-4 py-2 rounded hover:bg-green-700"
        >
          {fetching ? "Fetching..." : "Fetch Books"}
        </button>
      </div>
    </div>

      {/* Loading */}
      {loading && (
        <p className="text-gray-400">Loading books...</p>
      )}

      {/* Empty */}
      {!loading && books.length === 0 && (
        <p className="text-gray-400">
          No books found. Click "Fetch Books" to load data.
        </p>
      )}

      {/* Books Grid */}
      {!loading && books.length > 0 && (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
          {books.map((book) => (
            <BookCard
              key={book.id}
              book={book}
              onClick={onSelectBook}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default Home;