import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    print("Data Loaded Successfully!")
    print(df.head())
    return df
