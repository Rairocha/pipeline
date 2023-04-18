import pandas as pd

def carregar(df,nome,engine):
    df.to_sql(nome, engine, index = False, if_exists = 'replace')