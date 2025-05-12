import streamlit as st
import pandas as pd
from DataClean import data

st.title("Patients with Outstanding Balances")

out_bal = 0
out_bal_count = 0
for i, row in data.iterrows():             # only counting approved balances
    if row['Request Status'] == "Approved":
        if row[' Remaining Balance '] > 0:     # outstanding balances - so excluding negatives
            out_bal += row[' Remaining Balance ']  # sum total $
            out_bal_count += 1                     # count # of patients

st.write("Number of patients with an outstanding balance:", out_bal_count)
st.write("Total outstanding balance: $", round(out_bal, 2))
st.write("Average outstanding balance: $", round(out_bal / out_bal_count, 2))
st.write("(For approved requests only)")

average_assist = {}
for i in data['Type of Assistance (CLASS)'].unique():           # for each type of assistance
    average_assist[i] = data.loc[data['Type of Assistance (CLASS)'] == i, " Amount "].mean() # mean per type
    average_assist[i] = round(average_assist[i], 2)

avg_ast_df = pd.DataFrame(average_assist, index=[0, len(average_assist)-1])
avg_ast_df = avg_ast_df.T
avg_ast_df = avg_ast_df.drop(avg_ast_df.columns[1] , axis=1)      # again column formatting/presentation issues
st.write("Average $ Amount of Assistance per type of Assistance Provided")
st.write(avg_ast_df.T)