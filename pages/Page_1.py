import streamlit as st
from DataClean import data

st_data =  data

st.title("Applications for Review")


need_review = st_data[st_data['Application Signed?'] == "No"]
st.dataframe(need_review)


#st.dataframe(st_data)