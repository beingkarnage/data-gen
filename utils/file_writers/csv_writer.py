def csvWriter(df, params):
    df.to_csv(**params,index=False)