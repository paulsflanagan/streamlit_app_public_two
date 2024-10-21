import streamlit as st

st.title('Streamlit App Public - Two')

try:
  url = st.query_params["url"]
  st.write("URL FOUND" + url)
except:
  st.write("URL NOT FOUND")
