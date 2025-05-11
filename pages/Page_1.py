import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt
from DataClean import data

st_data =  data

st.title("Hope Foundation Dashboard")
alt.themes.enable('dark')
st.sidebar.subheader("Dashboard")
# with st.sidebar:
#     st.title("Applications")
#
#     need_review = st_data[st_data['Application Signed?'] == "No"]
#     st.dataframe(need_review)


#st.dataframe(st_data)