import pandas as pd
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/SamEdstrand/ECON-8320-Semester-Project/refs/heads/main/Data%20-%202.csv')

#remove unnecessary white spaces
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].str.strip()

# clean city data
for i, row in data.iterrows():
    city = row['Pt City']
    if city == '' or type(city) != str:
        city = "Missing"
    city = str(city)
    city = city.lower()
    city = city.title()
    data.at[i, 'Pt City'] = city

#print(data['Pt City'].sample(10))

#st.write(data.head(25))


