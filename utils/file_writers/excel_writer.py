def excelWriter(df, params):
    df.to_excel(**params)
