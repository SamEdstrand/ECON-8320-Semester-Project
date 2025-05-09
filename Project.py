import pandas as pd
import regex as re
import streamlit as st
from OtherInfo import states, state_names2

data = pd.read_csv('https://raw.githubusercontent.com/SamEdstrand/ECON-8320-Semester-Project/refs/heads/main/Data%20-%202.csv')

# clean data
for i, row in data.iterrows():

    patient_id = row['Patient ID#'] # pull patient ID line item
    patient_id = str(patient_id) # convert to string
    patient_id = patient_id.strip() # strip whitespace
    if patient_id == '':
        patient_id = "Missing" # make missing data consistent
    if patient_id != "Missing" and not re.search(r'\d{6}', patient_id):
        patient_id = "Error: Not a valid Patient ID" # confirm that ID is either missing or conforms to pattern
    data.at[i, 'Patient ID#'] = patient_id # replace ID line item


    request_date = row['Grant Req Date'] # pull grant request line item
    if request_date == '':
        request_date = "Missing" # make missing data consistent
    request_date = str(request_date)  # convert to string
    request_date = request_date.strip() # remove whitespace
    if re.search(r'^(([0][1-9]|[1-2][0-9]|[3][0-1])-([0][1-9]|[1][0-2])-(\d\d\d\d))$', request_date):
        #request_date = f"{request_date[0:1]}/{request_date[3:4]}/{request_date[6:9]}"
        request_date = request_date.replace("-", "/")  # replace dashes with slashes
    if re.search(r'^(([0][1-9]|[1-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/(\d\d\d\d))$', request_date):
        request_date = "Error: Not a valid Grant Req Date"        # if grant request doesnt match DD/MM/YYYY
    data.at[i, 'Grant Req Date'] = request_date # replace grant request date line item


    app_year = row['App Year'] # pull app year line item
    if app_year == '':
        app_year = "Missing" # make missing data consistent
    if app_year != "Missing":
        app_year = int(app_year) # convert to integers
    if app_year != 1 or app_year != 2 or app_year != 3:
        app_year = "Error: Not a valid App Year" #check for integers within logical range
    data.at[i, 'App Year'] = app_year  # replace app_year line item


    balance = row[' Remaining Balance '] # pull remaining balance line item
    balance = str(balance)           # convert to string
    balance = balance.strip()        # remove whitespace
    balance = balance.replace("$","") # replace $
    balance = balance.replace(",","")   # replace commas
    balance = balance.replace("-","0")    # convert dashes to 0
    if "(" in balance:                    # check for negatives
        balance = balance.replace("(", "").replace(")", "")    # replace parantheses
        try:                                        
            balance = round(float(balance),2)           # convert to float, round to 2 decimals
            balance *= -1                             # reinstate negative balance
        except:
            balance = "Error: Not a valid Balance"
    else:                                        # for positive balances
        try:
            balance = round(float(balance),2)         # convert to float, round 2 decimals
        except:
            balance = "Error: Not a valid Balance"
    data.at[i, ' Remaining Balance '] = balance     # replace balance line item


    request_status = row['Request Status'] # pull request status line item
    request_status = str(request_status)           # convert to string
    if request_status == "":
        request_status = "Missing"               # make missing data consistent
    request_status = request_status.strip()      # remove whitespace
    request_status = request_status.lower()
    request_status = request_status.title()      # make capitalization consistent
    request_status = re.sub(r'[^a-zA-Z]', '', request_status)    # remove special characters
    if request_status != "Approved" and request_status != "Pending" and request_status != "Denied" and request_status != "Missing":
        request_status = "Error: Not a valid Request Status"
    data.at[i, 'Request Status'] = request_status  # replace line item

    payment_status = row['Payment Submitted?']  # return payment submitted line item
    payment_status = str(payment_status)      # convert to string
    payment_status = payment_status.strip()       # remove whitespace
    
    


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
    if state == '' or type(state) != str:
        state = "Missing"  # make empty data consistent
    state = state.strip()
    if len(state) != 2 and state != "Missing": # checking for states entered as state names themselves
        state = state.lower()
        state = state.title()              # make formatting consistent
        try:
            state = state_names2[state] # convert names to abbreviations
        except:
            state = "Error: Not US State" # if text is not a state
    if len(state) == 2:
        state = state.upper()
        if state not in states:
            state = "Error: Not US State" # checks that state value is equal to state abbrev
    data.at[i, 'Pt State'] = state


    zipcode = row['Pt Zip'] #pull zipcode line item
    if zipcode == '':
        zipcode = "Missing" # make miss data consistent
    try:
        zipcode = str(zipcode) # convert to string for regex check
    except:
        zipcode = "Error: Not a valid Zip Code"
    zipcode = zipcode.strip()     # remove whitespace
    if zipcode != 'Missing' and not re.search(r'^\d{5}(?:[-\s]\d{4})?$', zipcode):
        zipcode = "Error: Not a valid Zip Code"  # differentiate between missing and incorrect data
    data.at[i, 'Pt Zip'] = zipcode   # replace zip code line item




print(data['Grant Req Date'].sample(10))
print(data['Grant Req Date'].unique())
print(len(data['Grant Req Date'].unique()))



#st.write(data.head(25))


