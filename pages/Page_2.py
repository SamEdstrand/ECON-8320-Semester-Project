import streamlit as st
from DataClean import data

st.title('Page 2')
st.write(data.sample(25))