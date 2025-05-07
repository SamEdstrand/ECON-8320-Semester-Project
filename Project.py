import pandas as pd
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/SamEdstrand/ECON-8320-Semester-Project/refs/heads/main/Data%20-%202.csv')

print(data['Gender'].sample(10))

st.write(data.head(25))


