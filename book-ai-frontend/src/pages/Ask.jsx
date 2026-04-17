// Ask page component
import { useState } from "react";
import { askQuestion } from "../api/api";
import AnswerBox from "../components/AnswerBox";

function Ask() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question) return;

    setLoading(true);
    const res = await askQuestion(question);
    setResult(res.data);
    setLoading(false);
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">🤖 Ask AI</h1>

      <div className="flex gap-2">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask about books..."
          className="flex-1 p-3 rounded bg-gray-800 text-white"
        />

        <button
          onClick={handleAsk}
          className="bg-blue-600 px-5 rounded"
        >
          Ask
        </button>
      </div>

      {loading && <p className="mt-4">Thinking...</p>}

      <AnswerBox result={result} />
    </div>
  );
}

export default Ask;