import streamlit as st
import shortuuid
import requests

# In-memory storage for URL mapping
url_mapping = {}

def shorten_url(url):
    short_id = shortuuid.uuid()[:8]
    url_mapping[short_id] = url
    return short_id

def get_original_url(short_id):
    return url_mapping.get(short_id)

st.title("URL Shortener")

url_input = st.text_input("Enter a URL to shorten:")

if url_input:
    if not url_input.startswith(('http://', 'https://')):
        url_input = 'https://' + url_input
    
    short_id = shorten_url(url_input)
    shortened_url = f"http://yourdomain.com/r/{short_id}"
    
    st.success(f"Shortened URL: {shortened_url}")
    st.markdown(f"[{shortened_url}]({url_input})")

st.markdown("---")

st.subheader("Retrieve Original URL")
short_id_input = st.text_input("Enter the short ID:")

if short_id_input:
    original_url = get_original_url(short_id_input)
    if original_url:
        st.success(f"Original URL: {original_url}")
        st.markdown(f"[{original_url}]({original_url})")
    else:
        st.error("Short ID not found.")