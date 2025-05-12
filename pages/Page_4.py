import streamlit as st
import pandas as pd
import numpy as np
from DataClean import data

st.title("Summary")


year = {'18':'', '19':'', '20':'', '21':'', '22':'', '23':'', '24':'', '25':''}
year_keys = ['18','19','20','21','22','23','24','25']

for x in year_keys:
    sum = 0
    for i, row in data.iterrows():
        if row["Grant Req Date"][-2:] == x:
            if row[" Amount "] >0:
                sum += row[' Amount ']
    year[x] = sum

year_by_year_df = pd.DataFrame(year, index=[0, len(year)-1])
year_by_year_df = year_by_year_df.T
year_by_year_df = year_by_year_df.drop(year_by_year_df.columns[1], axis =1)
st.write("Total $ worth of assistance provided annually")
st.bar_chart(year_by_year_df)

total = 0
for a in year:
    total += year[a]
st.write("Cumulative assistance provided: $", round(total,2))