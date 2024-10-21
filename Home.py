import streamlit as st

st.title('Streamlit App Public - Two')

if st.query_params["url"]:
  st.write("URL FOUND")
else:
  st.write("URL NOT FOUND")
