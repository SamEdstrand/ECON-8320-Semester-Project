import streamlit as st
import pandas as pd
from Main import run # import dataframe from original Data Clean file

st.title("Demographic Analysis")
data = run()

city_dict = {}
for i in data['Pt City'].unique():   # for each individual city
    city_dict[i] = data.loc[data['Pt City'] == i, ' Amount '].sum() # sum the amount of assistance, add to dictionary

city_df = pd.DataFrame(city_dict, index=[0, len(city_dict)-1]) # convert to dataframe
st.write('$ Amount of assistance provided by city')
city_df = city_df.T                     #transposing and dropping because I was getting an extra column
city_df = city_df.drop(city_df.columns[1] , axis=1) # probably did something wrong with the index
st.write(city_df)

gender_dict = {}
for i in data['Gender'].unique():
    gender_dict[i] = data.loc[data['Gender'] == i, ' Amount '].sum()

gender_df = pd.DataFrame(gender_dict, index=[0, len(gender_dict)-1])  # same as city process above
st.write('$ Amount of assistance provided by gender')
gender_df = gender_df.T
gender_df = gender_df.drop(gender_df.columns[1] , axis=1)
st.write(gender_df.T)                                     # transpose again for presentation

ins_dict = {}
for i in data['Insurance Type'].unique():
    if i == "Nan":
        i = "Missing"                   # convert for reporting consistency, messed up on data cleaning
    ins_dict[i] = data.loc[data['Insurance Type'] == i, ' Amount '].sum() # sum by each insurance type

ins_df = pd.DataFrame(ins_dict, index=[0, len(ins_dict)-1])
st.write("$ Amount of assistance provided by insurance type ")
ins_df = ins_df.T
ins_df = ins_df.drop(ins_df.columns[1] , axis=1) # same as above
st.write(ins_df.T)