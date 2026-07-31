def summarize_chunk(chunk, client):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            { 
                "role": "system", 
                "content": """You are a precise summarizer. Extract the core facts, \
                    arguments, and conclusions from the text. Keep it to 3-4 sentences.
                    """
            },
            {
                "role": "user",
                "content": f"Summarize this text:\n\n{chunk}"
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content