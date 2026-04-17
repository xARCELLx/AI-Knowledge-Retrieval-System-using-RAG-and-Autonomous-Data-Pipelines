import { useState } from "react";
import Home from "./pages/Home";
import Ask from "./pages/Ask";
import BookDetail from "./pages/BookDetail";

function App() {
  const [page, setPage] = useState("home");
  const [selectedBook, setSelectedBook] = useState(null);

  const openBook = (book) => {
    setSelectedBook(book);
    setPage("detail");
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      {/* Navbar */}
      <div className="flex gap-4 mb-6">
        <button onClick={() => setPage("home")}>
          📚 Books
        </button>
        <button onClick={() => setPage("ask")}>
          🤖 Ask AI
        </button>
      </div>

      {/* Pages */}
      {page === "home" && (
        <Home onSelectBook={openBook} />
      )}

      {page === "ask" && <Ask />}

      {page === "detail" && (
        <BookDetail
          book={selectedBook}
          goBack={() => setPage("home")}
        />
      )}
    </div>
  );
}

export default App;