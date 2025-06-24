import pandas as pd

def load_data(filepath):
    """
    Loads the sales dataset and performs initial cleaning:
    - Drops duplicates
    - Converts date columns to datetime format
    """
    df = pd.read_csv(filepath, encoding='latin1')
    df.drop_duplicates(inplace=True)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    return df
