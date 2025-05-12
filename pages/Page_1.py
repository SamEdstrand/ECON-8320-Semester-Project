import streamlit as st
from DataClean import data

st_data =  data  # import dataframe from original Data Clean file

st.title("Applications for Review")


need_review = st_data[st_data['Request Status'] == "Pending"]  # pull rows with applications marked "Pending"
st.dataframe(need_review)


#st.dataframe(st_data)