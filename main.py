import streamlit as st
from scrape import (scrape_website,split_dom_content,clean_body_content,extract_body)
from bs4 import BeautifulSoup
from parse import parse_with_ollama

st.title("AI web scraper")
url = st.text_input("Enter the URL of the webpage you want to scrape")


if st.button("Scrape Site"):
    st.write("scraping website")
    result=scrape_website(url)
    body_content = extract_body(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content",cleaned_content,height=300)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)