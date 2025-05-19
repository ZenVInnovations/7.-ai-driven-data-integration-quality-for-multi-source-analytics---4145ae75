import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_text(text):
    return str(text).strip().lower()

def preprocess(df, name_col, email_col):
    df[name_col] = df[name_col].apply(normalize_text)
    df[email_col] = df[email_col].apply(normalize_text)
    return df
