import streamlit as st
import pandas as pd
from Main import run

st.title("Summary")
data = run()

year = {'18':'', '19':'', '20':'', '21':'', '22':'', '23':'', '24':'', '25':''} # store for sums
year_keys = ['18','19','20','21','22','23','24','25']  # index for loop

for x in year_keys:
    sum = 0
    for i, row in data.iterrows():
        if row["Grant Req Date"][-2:] == x:   # if grant date ends with last 2 digits of each year
            if row[" Amount "] >0:            # only include positive amounts
                sum += row[' Amount ']
    year[x] = sum

year_by_year_df = pd.DataFrame(year, index=[0, len(year)-1])
year_by_year_df = year_by_year_df.T
year_by_year_df = year_by_year_df.drop(year_by_year_df.columns[1], axis =1) # formatting concerns again
st.write("Total $ worth of assistance provided annually")
st.bar_chart(year_by_year_df)

total = 0
for a in year:
    total += year[a]         # find the total of $ sums from dictionary
st.write("Cumulative assistance provided: $", round(total,2))