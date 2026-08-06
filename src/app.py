import streamlit as st
from summarizer.engine import summarize_website

st.set_page_config(page_title="Summa-Crawl")
st.title("📄 Summa-Crawl")
st.subheader("Summarize websites with AI")

url = st.text_input("Enter the URL of the article or page you want to summarize:")

if st.button("Summarize") and url:
    with st.spinner("🧠 Crawling and summarizing... this takes about 10-15 seconds."):
        result = summarize_website(url)
        st.markdown("### 📝 Summary")
        st.write(result)