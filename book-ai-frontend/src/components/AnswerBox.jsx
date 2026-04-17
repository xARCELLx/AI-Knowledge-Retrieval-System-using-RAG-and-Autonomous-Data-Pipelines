function AnswerBox({ result }) {
  if (!result) return null;

  // 🔥 Pick first source as main reference
  const mainSource = result.sources?.[0];

  return (
    <div className="mt-6 bg-gray-800 p-5 rounded-xl space-y-4">
      
      {/* 🤖 Answer */}
      <div>
        <h2 className="text-xl font-bold mb-1">🤖 Answer</h2>
        <p className="text-gray-300">{result.answer}</p>
      </div>

      {/* 🏷️ Genre */}
      {mainSource?.genre && (
        <div>
          <h2 className="font-semibold">🏷️ Genre</h2>
          <p className="text-green-400">{mainSource.genre}</p>
        </div>
      )}

      {/* 🤝 Recommendations */}
      {result.sources.length > 1 && (
        <div>
          <h2 className="font-semibold">🤝 Recommendations</h2>
          <ul className="list-disc ml-5 text-gray-300">
            {result.sources.slice(1).map((src, i) => (
              <li key={i}>{src.title}</li>
            ))}
          </ul>
        </div>
      )}

      {/* 📖 Sources */}
      <div>
        <h2 className="font-semibold">📖 Sources</h2>
        <div className="space-y-2">
          {result.sources.map((src, i) => (
            <div key={i} className="bg-gray-700 p-3 rounded">
              <p className="font-semibold">{src.title}</p>
              <p className="text-xs text-gray-400">
                {src.excerpt}
              </p>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
}

export default AnswerBox;