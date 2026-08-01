def split_into_chunks(text, chunk_size=2000, overlap=200):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        # If we aren't at the end, find the nearest period/space to avoid cutting words
        if end < len(text):
            # Look for a period or newline within the last 200 chars
            last_period = text.rfind('.', start, end)
            last_space = text.rfind(' ', start, end)
            cut_point = max(last_period, last_space)

            if start < cut_point:
                end = cut_point + 1

        chunk = text[start:end].strip()
        chunks.append(chunk)

        # move start back by overlap amount to maintain context
        start = end - overlap

    return chunks
