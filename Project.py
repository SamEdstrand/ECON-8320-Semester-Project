import pandas as pd
import numpy as np
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
    if re.match(r'^(([1-9]|[1][0-2])-([1-9]|[1-2][0-9]|[3][0-1])-(\d\d))$', request_date):
        #request_date = f"{request_date[0:1]}/{request_date[3:4]}/{request_date[6:9]}"
        request_date = request_date.replace("-", "/")  # replace dashes with slashes
    if not re.match(r'^(([1-9]|[1][0-2])\/([1-9]|[1-2][0-9]|[3][0-1])\/(\d\d))$', request_date) and request_date != "Missing":
        request_date = "Error: Not a valid Grant Req Date"        # if grant request doesnt match DD/MM/YYYY
    data.at[i, 'Grant Req Date'] = request_date # replace grant request date line item


    app_year = row['App Year'] # pull app year line item
    if app_year == '':
        app_year = "Missing" # make missing data consistent
    if app_year != "Missing":
        app_year = int(app_year) # convert to integers
    if app_year != 1 and app_year != 2 and app_year != 3:
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
    payment_status = payment_status.strip() # remove whitespace
    if payment_status == "":
        payment_status = "Missing"         # make missing data consistent
    if re.search(r'^(([1-9]|[1][0-2])-([1-9]|[1-2][0-9]|[3][0-1])-(\d\d))$', payment_status):
        payment_status = payment_status.replace("-", "/")  # replace dashes with slashes
    if not re.search(r'^(([1-9]|[1][0-2])\/([1-9]|[1-2][0-9]|[3][0-1])\/(\d\d))$', payment_status):
        payment_status = payment_status.lower()
        payment_status = payment_status.title()                 # make formatting consistent
        if payment_status != "Yes" and payment_status != "No" and payment_status != "Missing":        # only "Yes" or "No" if not date
            payment_status = "Error: Not a valid Payment Status"
    data.at[i, 'Payment Submitted?'] = payment_status          # replace line item


    reason = row['Reason - Pending/No']     # make sure reason is text
    if type(reason) != str:
        reason = ""
    reason.strip()
    data.at[i, 'Reason - Pending/No'] = reason


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
        zipcode = "Missing" # make missing data consistent
    try:
        zipcode = str(zipcode) # convert to string for regex check
    except:
        zipcode = "Error: Not a valid Zip Code"
    zipcode = zipcode.strip()     # remove whitespace
    if zipcode != 'Missing' and not re.search(r'^\d{5}(?:[-\s]\d{4})?$', zipcode):
        zipcode = "Error: Not a valid Zip Code"  # differentiate between missing and incorrect data
    data.at[i, 'Pt Zip'] = zipcode   # replace zip code line item


    language = row['Language']     # pull languge line item
    if language == '' or type(language) != str:     # make missing data consistent
        language = "Missing"
    language = language.strip()   # remove whitespace
    language = language.title()   # capitalize
    data.at[i, 'Language'] = language # replace line item


    DOB = row['DOB'] # pull date of birth
    if DOB == '':
        DOB = "Missing"           # make missing data consistent
    DOB = str(DOB)  # convert to string
    DOB = DOB.strip() # remove whitespace
    if re.match(r'^(([1-9]|[1][0-2])-([1-9]|[1-2][0-9]|[3][0-1])-(\d\d|\d\d\d\d))$', DOB): #allow for 2 or 4 digit years
        DOB = request_date.replace("-", "/")  # replace dashes with slashes
    if not re.match(r'^(([1-9]|[1][0-2])\/([1-9]|[1-2][0-9]|[3][0-1])\/(\d\d|\d\d\d\d))$', DOB) and DOB != "Missing":
        DOB = "Error: Not a valid Date of Birth"        # if DOB grant request doesnt match DD/MM/YYYY
    data.at[i, 'DOB'] = DOB # replace line item


    maritial_status = row['Marital Status']   # pull maritial status line item
    maritial_status = str(maritial_status)
    if maritial_status == '':
        maritial_status = "Missing"     # make missing data consistent
    if maritial_status[0:3]  == "Sep":
        maritial_status = "Separated"   # fixed spelling error for separated
    maritial_status = maritial_status.strip()  # remove whitespace
    maritial_status = maritial_status.title()    # consistent capitalization
    data.at[i, 'Marital Status'] = maritial_status    # replace line item


    gender = row['Gender']    # pull gender line item
    gender = str(gender)
    gender = gender.strip()   # remove whitespace
    gender = gender.title()   # make capitalization consistent
    if gender == '':
        gender = "Missing"    # make missing data consistent
    if gender[0] == "M":
        gender = "Male"       # make male consistent
    elif gender[0] == "F":
        gender = "Female"     # make female consistent]
    data.at[i, 'Gender'] = gender # replace line item


    race = row['Race']  # pull race line item
    race = str(race)    # convert to string
    race = race.strip()  # remove whitespace
    race = race.title()   # make capitalization consistent
    if race == '':
        race = "Missing"  # make missing data consistent
    if race[0:15] == "American Indian":            # fix inconsistency
        race = "American Indian Or Alaska Native"
    if race[0:3] == "Whi":             # fix inconsistency
        race = "White"
    data.at[i, 'Race'] = race              # replace line item


    hispanic = row['Hispanic/Latino'] # pull line item
    hispanic = str(hispanic)         # convert to string
    if hispanic == '':               # make missing data consistent
        hispanic = "Missing"
    hispanic = hispanic.strip()      # remove whitespace
    hispanic = hispanic.title()      # make capitalization consistent
    if hispanic[0:1]  == "H" or hispanic[0:1] == "Y":
        hispanic = "Yes"             # account for all yes answers
    elif hispanic[0:1] == "N":       # account for all no answers
        hispanic = "No"
    elif hispanic !=  "Missing":        # otherwise
        hispanic = "Decline to answer"
    data.at[i, 'Hispanic/Latino'] = hispanic # replace line item


    sexuality = row['Sexual Orientation']    # pull line item
    sexuality = str(sexuality)  # convert to string
    sexuality = sexuality.strip()  # remove whitespace
    sexuality = sexuality.title()  # make capitalization consistent
    if sexuality[0:2] ==  "St" or sexuality[0:3] == "Het":
        sexuality = "Heterosexual"    # fix spelling and inconsistency
    elif sexuality[0:3] == "Gay" or sexuality[0:3] == "Les" or sexuality[0:3] == "Hom" or sexuality[0:3] == "Que":
        sexuality = "Homosexual"
    elif sexuality[0:2] == "Bi":
        sexuality = "Bisexual"
    elif sexuality[0:2] == "As":
        sexuality = "Asexual"                   # check options
    elif sexuality[0:3] == "Dec":
        sexuality = "Decline to answer"
    else:
        sexuality = "Missing"
    data.at[i, 'Sexuality'] = sexuality  # replace line item


    insurance = row['Insurance Type']     # pull insurance line item
    insurance = str(insurance)
    insurance = insurance.strip()
    insurance = insurance.title()
    if insurance == '' or insurance == "Unknown":      # make missing data consistent
        insurance = "Missing"
    elif insurance[0:3] == "Uni":     # fixing uninsured typos
        insurance = "Uninsured"
    data.at[i, 'Insurance Type'] = insurance      # replace line item


    household_size = row['Household Size']    # pull household size
    if household_size == '':
        household_size = "Missing"
    if household_size != "Missing":
        try:
            household_size = int(household_size)      # attempt convert to integer
            if household_size > 25:                               # check that household size is reasonable
                household_size = "Error: Invalid Household Size"
        except ValueError:
            household_size = "Error: Invalid Household Size"  # if not missing or integer, assumed to be an error
    data.at[i, 'Household Size'] = household_size # replace line item

    h_income = row[' Total Household Gross Monthly Income '] # pull income line item
    h_income = str(h_income)           # convert to string
    h_income = h_income.strip()        # remove whitespace
    if h_income == '':
        h_income = "Missing"                 # make missing data consistent and known
    h_income = h_income.replace("$","") # replace $
    h_income = h_income.replace(",","")   # replace commas
    h_income = h_income.replace("-","0")    # convert dashes to 0
    if "(" in h_income:                    # check for negatives
        h_income = h_income.replace("(", "").replace(")", "")    # replace parantheses
        try:
            h_income = round(float(h_income),2)           # convert to float, roun
            h_income *= -1                             # reinstate negative balan
        except:
            h_income = "Error: Not a valid Balance"
    elif h_income != "Missing":                                # for positive balances
        try:
            h_income = round(float(balance),2)         # convert to float, round
        except:
            h_income = "Error: Not a valid Balance"
    data.at[i, ' Total Household Gross Monthly Income '] = h_income     # replace income line item


    distance = row['Distance roundtrip/Tx']        # pull distance line item
    if distance == '' or distance == "N/A":        # make missing data consistent
        distance = "Missing"
    distance = str(distance)
    distance = distance.strip()
    distance = distance.title()                  # make capitalization consistent
    if distance[0:1] == "U" :                  # unknown data
        distance = "Unknown"
    elif distance != "Missing":
        try:                                        # attempt conversion to float
            distance = round(float(distance),1)
        except:
            distance = "Error: Not a valid Distance"      # either unknown, missing or number
    data.at[i, 'Distance roundtrip/Tx'] = distance   # replace line item


    referral = row['Referral Source']   # pull referral line item
    referral = str(referral)             # convert to string
    referral = referral.strip()             # remove whitespace
    referral = referral.title()              # make capitalization consistent
    data.at[i, 'Referral Source'] = referral  # replace line item


    referral2 = row['Referred By:']  # pull referred by
    referral2 = str(referral2)                 # convert to string
    referral2 = referral2.strip()                 # remove whitespace
    referral2 = referral2.title()                  # make capitalization cons
    data.at[i, 'Referred By:'] = referral2       # replace line item
    

    assitance = row['Type of Assistance (CLASS)']




print(data['Distance roundtrip/Tx'].unique())
print(data['Distance roundtrip/Tx'].sample(10))
print(len(data['Distance roundtrip/Tx'].unique()))


#st.write(data.head(25))


