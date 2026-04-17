from books.services.ai_service import client


def classify_genre(text: str):
    try:
        prompt = f"""
        You are a book classification system.

        Classify the genre of the book STRICTLY into ONE of these categories:
        Fantasy, Romance, Science Fiction, Mystery, Thriller, Horror, Historical, Adventure, Drama, Comedy

        Rules:
        - Return ONLY one word
        - Do NOT explain
        - Do NOT say Unknown unless impossible

        Text:
        {text}

        Genre:
        """

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[
                {"role": "user", "content": prompt}
            ],
            extra_body={"max_tokens": 20}
        )

        genre = response.choices[0].message.content.strip()

        return genre

    except Exception as e:
        print("Genre classification error:", e)
        return "Unknown"