# books/services/rag_service.py

from books.services.embedding_service import generate_embedding
from books.services.vector_db import query_similar
from books.services.ai_service import client
from books.models import Book


def ask_question(question: str):
    try:
        print(f"\n🔍 Question: {question}")

        # 1. Generate embedding
        query_embedding = generate_embedding(question)

        # 2. Retrieve similar chunks
        results = query_similar(query_embedding, n_results=3)

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        if not documents:
            return {
                "answer": "I don't have enough information.",
                "sources": []
            }

        # 3. Build context
        context = "\n\n".join(documents)

        print("📚 Retrieved Context:")
        print(context)

        # 4. STRICT RAG PROMPT
        prompt = f"""
You are a strict AI assistant.

answer according to given context.
Rules:
- If the answer is not in the context, say "I don't know" ( i don't care if you know the answer but if the answer is no where around the context, you MUST say you don't know , for example if the question is about who is the president of the US but the context doesn't mention anything about the US president, you MUST say you don't know )

Context:
{context}

Question:
{question}

Answer:
"""

        # 5. Generate answer
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[
                {"role": "user", "content": prompt}
            ],
            extra_body={"max_tokens": 200}
        )

        answer = response.choices[0].message.content.strip()

        # 6. Build CLEAN sources 
        sources = []

        for doc, meta in zip(documents, metadatas):
            book_id = meta.get("book_id")

            try:
                book = Book.objects.get(id=book_id)

                sources.append({
                    "title": book.title,
                    "excerpt": doc[:200],
                    "summary": book.summary,
                    "genre": book.genre
                })

            except Book.DoesNotExist:
                continue

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}",
            "sources": []
        }