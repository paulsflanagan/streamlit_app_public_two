import streamlit as st

st.title('Streamlit App Public - Two')

try:
  url = st.query_params["url"]
  st.write("URL FOUND " + url)

  if url == "1234":
    st.write("Success")
  else:
    st.write("Failure")
except:
  st.write("Failure no url")
