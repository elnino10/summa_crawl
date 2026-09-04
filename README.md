# Summa Crawl

AI-powered website summarizer. Paste a page URL and get a short, cohesive overview of the article or post.

**Live app:** [https://summacrawl.streamlit.app/](https://summacrawl.streamlit.app/)

## How it works

The pipeline is a map-reduce summarization flow:

1. **Crawl** — fetch the page, strip boilerplate (`script`, `style`, `nav`, `header`, `footer`), and extract paragraph text.
2. **Split** — break the text into overlapping chunks (~2000 characters, 200-character overlap) at sentence or word boundaries so long pages fit the model context.
3. **Map** — summarize each chunk with GPT-4o-mini (core facts, arguments, conclusions).
4. **Reduce** — combine those chunk summaries into a 3-paragraph overview.

## Project structure

```
summa_crawl/
├── src/
│   ├── app.py                 # Streamlit UI
│   ├── crawler/scraper.py     # Fetch and extract page text
│   ├── processor/splitter.py  # Chunk long text
│   ├── summarizer/engine.py   # Orchestrate crawl → split → summarize
│   └── utils/helpers.py       # Per-chunk OpenAI calls
├── main.py                    # Optional CLI entry point
└── pyproject.toml
```

## Requirements

- Python 3.12+
- An [OpenAI API key](https://platform.openai.com/api-keys)
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Local setup

```bash
git clone https://github.com/elnino10/summa_crawl.git
cd summa_crawl
uv sync
```

Create a `.env` file in the project root (this file is gitignored):

```bash
OPENAI_API_KEY=sk-...
```

On Streamlit Community Cloud, set the same key under **Settings → Secrets** instead of committing `.env`.

## Run the app

From the project root:

```bash
uv run streamlit run src/app.py
```

## CLI

```bash
uv run python main.py
```

You will be prompted for a URL; the summary is printed to the terminal.

## Notes and limits

- Extraction relies on `<p>` tags, so pages that render content mainly with JavaScript or non-paragraph markup may return little or no text.
- Pages with fewer than ~100 characters of extracted text are rejected.
- Summarization calls OpenAI (`gpt-4o-mini`) and needs outbound HTTPS access.
- Do not commit `.env` or API keys.
