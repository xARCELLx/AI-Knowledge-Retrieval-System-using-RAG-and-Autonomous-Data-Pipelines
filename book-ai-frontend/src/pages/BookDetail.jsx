import { useEffect, useState } from "react";
import { getRecommendations } from "../api/api";

function BookDetail({ book, goBack }) {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    if (!book) return;

    getRecommendations(book.id)
      .then((res) => {
        setRecommendations(res.data);
      })
      .catch((err) => console.error(err));
  }, [book]);

  if (!book) return <p>No book selected</p>;

  return (
    <div>
      <button
        onClick={goBack}
        className="mb-4 text-blue-400"
      >
        ← Back
      </button>

      {/* Book Info */}
      <div className="bg-gray-800 p-6 rounded-xl">
        <h1 className="text-2xl font-bold">{book.title}</h1>
        <p className="text-gray-400">{book.author}</p>

        <p className="mt-4 text-gray-300">
          {book.description}
        </p>

        <p className="mt-4">
          <span className="text-green-400">Genre:</span>{" "}
          {book.genre}
        </p>

        <p className="mt-4 text-sm text-gray-400">
          {book.summary}
        </p>
      </div>

      {/* Recommendations */}
      <div className="mt-6">
        <h2 className="text-xl font-bold mb-3">
          🤝 Similar Books
        </h2>

        {recommendations.length === 0 ? (
          <p className="text-gray-400">
            No recommendations found
          </p>
        ) : (
          <div className="grid md:grid-cols-2 gap-4">
            {recommendations.map((rec) => (
              <div
                key={rec.id}
                className="bg-gray-800 p-4 rounded-xl"
              >
                <h3 className="font-semibold">
                  {rec.title}
                </h3>
                <p className="text-sm text-gray-400">
                  {rec.author}
                </p>
                <p className="text-xs mt-2">
                  {rec.summary?.slice(0, 100)}...
                </p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default BookDetail;