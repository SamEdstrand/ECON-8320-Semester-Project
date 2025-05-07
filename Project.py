import pandas as pd
import streamlit as st

data = pd.read_excel('/Users/mainfolder/Documents/UNO Service Learning Data Sheet De-Identified Version.xlsx')

print(data['Gender'].sample(10))

st.write(data.head(25))


