import pandas as pd
import regex as re
import streamlit as st
from OtherInfo import states

data = pd.read_csv('https://raw.githubusercontent.com/SamEdstrand/ECON-8320-Semester-Project/refs/heads/main/Data%20-%202.csv')

# clean city data
for i, row in data.iterrows():
    city = row['Pt City'] # pull city line item
    if city == '' or type(city) != str:
        city = "Missing" # make empty data consistent
    city = str(city)     # make line item string
    city = city.strip()  # remove white spaces
    city = city.lower()  # make everything lower case
    city = city.title()  # Capitalize each word
    city = re.sub(r'[^a-zA-Z\s\.]', '', city) # remove any special characters besides '.'
    data.at[i, 'Pt City'] = city  # replace line item

    state = row['Pt State'] #pull state line item
    state = str(state) # convert line item to string
    if state == '' or type(state) != str:
        state = "Missing"  #make empty data consistent
    if len(state) != 2 and state != "Missing":
        state = "?" # states that don't conform to list
    if len(state) == 2:
        state = state.upper()
        if state not in states:
            state = "Error"
    data.at[i, 'Pt State'] = state



print(data['Pt State'].sample(10))
print(data['Pt State'].unique())
print(len(data['Pt State'].unique()))



#st.write(data.head(25))


