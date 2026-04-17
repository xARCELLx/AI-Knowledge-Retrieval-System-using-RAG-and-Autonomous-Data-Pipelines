function BookCard({ book, onClick }) {
  return (
    <div
      onClick={() => onClick(book)}
      className="bg-gray-800 p-5 rounded-2xl shadow-lg hover:scale-105 transition cursor-pointer"
    >
      {/* Title */}
      <h2 className="text-xl font-bold">{book.title}</h2>

      {/* Author */}
      <p className="text-gray-400">{book.author}</p>

      {/* ⭐ Rating */}
      <div className="mt-2 text-yellow-400 text-sm">
        {book.rating ? `⭐ ${book.rating}/5` : "⭐ No rating"}
      </div>

      {/* Summary */}
      <p className="mt-2 text-sm text-gray-300">
        {book.summary?.slice(0, 120)}...
      </p>

      {/* Footer */}
      <div className="mt-3 flex justify-between items-center">
        <span className="text-green-400 text-sm">
          {book.genre || "Unknown"}
        </span>

        <span className="text-blue-400 text-sm">
          View →
        </span>
      </div>
    </div>
  );
}

export default BookCard;