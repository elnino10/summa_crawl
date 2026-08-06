import os

from dotenv import load_dotenv
from openai import OpenAI
from crawler.scraper import crawl_website
from processor.splitter import split_into_chunks
from utils.helpers import summarize_chunk

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)


def summarize_website(url):
    # 1. Crawl
    raw_text = crawl_website(url)
    if raw_text.startswith("Error"):
        return raw_text
    
    # 2. Split
    chunks = split_into_chunks(raw_text)
    
    print(f"🔍 Crawled {len(raw_text)} characters, split into {len(chunks)} chunks.")
    
    # 3. Summarize each chunk (Map)
    chunk_summaries = []
    for i, chunk in enumerate(chunks):
        print(f"📝 Summarizing chunk {i+1}/{len(chunks)}...")
        summary = summarize_chunk(chunk, client)
        chunk_summaries.append(summary)
    
    # 4. Combine all chunk summaries into one final summary (Reduce)
    combined_text = " ".join(chunk_summaries)
    print("\n🧠 Creating final master summary...\n")
    
    final_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a synthesis expert. Combine the following bullet-point summaries into one cohesive, flowing 3-paragraph overview."},
            {"role": "user", "content": f"Combine these summaries:\n\n{combined_text}"}
        ],
        temperature=0.3
    )
    
    print(final_response.choices[0].message.content)
    return final_response.choices[0].message.content
