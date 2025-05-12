import pandas as pd
from DataClean_Function import clean
from DataClean import data

def update_data(csv):
    try:
        new_data = pd.read_csv(csv)
        new_data = clean(new_data)
        data = pd.concat([data, new_data], ignore_index=True)
        print(new_data.head())
    except FileNotFoundError:
        print("File not found", csv)
    except Exception as e:
        print("Error:", e)


print(data.head())