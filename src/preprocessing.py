from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.dropna()

    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    return df
