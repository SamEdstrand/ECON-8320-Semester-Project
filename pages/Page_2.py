import streamlit as st
import pandas as pd
from DataClean import data

st.title("Demographic Analysis")


city_dict = {}
for i in data['Pt City'].unique():
    city_dict[i] = data.loc[data['Pt City'] == i, ' Amount '].sum()

city_df = pd.DataFrame(city_dict, index=[0, len(city_dict)-1])
st.write('$ Amount of assistance provided by city')
city_df = city_df.T
city_df = city_df.drop(city_df.columns[1] , axis=1)
st.write(city_df)

gender_dict = {}
for i in data['Gender'].unique():
    gender_dict[i] = data.loc[data['Gender'] == i, ' Amount '].sum()

gender_df = pd.DataFrame(gender_dict, index=[0, len(gender_dict)-1])
st.write('$ Amount of assistance provided by gender')
gender_df = gender_df.T
gender_df = gender_df.drop(gender_df.columns[1] , axis=1)
st.write(gender_df.T)

ins_dict = {}
for i in data['Insurance Type'].unique():
    if i == "Nan":
        i = "Missing"
    ins_dict[i] = data.loc[data['Insurance Type'] == i, ' Amount '].sum()

ins_df = pd.DataFrame(ins_dict, index=[0, len(ins_dict)-1])
st.write("$ Amount of assistance provided by insurance type ")
ins_df = ins_df.T
ins_df = ins_df.drop(ins_df.columns[1] , axis=1)
st.write(ins_df.T)