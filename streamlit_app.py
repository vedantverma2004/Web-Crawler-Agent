import streamlit as st
from agent_logic import crawl_web

st.title("🕷️ Agentic Web Crawler")
url = st.text_input("Enter a URL to crawl:")

if url:
    st.write("Crawling:", url)
    result = crawl_web(url)
    st.subheader("Extracted Text")
    st.text(result["text"])
    st.subheader("Metadata")
    st.json(result["metadata"])
    st.subheader("Links")
    st.write(result["links"])
