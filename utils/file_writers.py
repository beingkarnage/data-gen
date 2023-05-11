def excelWriter(df, params):
    df.to_excel(**params)
def jsonWriter(df, params):
    df.to_json(**params)
def csvWriter(df, params):
    df.to_csv(**params)
def parquetWriter(df, **params):
    df.to_parquet(**params)
def sqlWriter(df, **params):
    df.to_sql(**params)