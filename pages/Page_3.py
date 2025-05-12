import streamlit as st
import pandas as pd
from DataClean import data

st.title("Patients with Outstanding Balances")

out_bal = 0
out_bal_count = 0
for i, row in data.iterrows():
    if row['Request Status'] == "Approved":
        if row[' Remaining Balance '] > 0:
            out_bal += row[' Remaining Balance ']
            out_bal_count += 1

st.write("Number of patients with an outstanding balance:", out_bal_count)
st.write("Total outstanding balance: $", round(out_bal, 2))
st.write("Average outstanding balance: $", round(out_bal / out_bal_count, 2))
st.write("For approved requests only")