import streamlit as st
from DataClean import data

st_data =  data

#st.title("Applications for Review")
st.set_page_config(page_title="Applications for Review", layout="wide", page_icon= "Requests")


need_review = st_data[st_data['Request Status'] == "Pending"]
st.dataframe(need_review)


#st.dataframe(st_data)