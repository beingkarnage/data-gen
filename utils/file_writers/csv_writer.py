def csvWriter(df, params):
    df.to_csv(**params)