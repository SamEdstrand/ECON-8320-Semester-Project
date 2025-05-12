import pandas as pd
from DataClean_Function import clean
from DataClean import data

file_name = input("Enter file name: ")

new_data = pd.read_csv(file_name)
new_data = clean(new_data)

data = pd.concat([data, new_data], ignore_index=True)