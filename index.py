import pandas as pd
from sqlalchemy import create_engine


def index_df1(date_value, time_value): 
    engine = create_engine('mysql+pymysql://mysql:0963@127.0.0.1:3306/shop')
    conn = engine.connect()
    df1 = pd.read_sql_table("dorm1",con=conn, index_col="요일")
    return "\n".join(df1[time_value][date_value].split()[:-4])

def index_df2(date_value, time_value): 
    engine = create_engine('mysql+pymysql://mysql:0963@127.0.0.1:3306/shop')
    conn = engine.connect()
    df2 = pd.read_sql_table("dorm2",con=conn, index_col="요일")
    return "\n".join(df2[time_value][date_value].split()[:-1])

def index_df3(date_value, time_value): 
    engine = create_engine('mysql+pymysql://mysql:0963@127.0.0.1:3306/shop')
    conn = engine.connect()
    df3 = pd.read_sql_table("dorm3",con=conn, index_col="요일")
    return "\n".join(df3[time_value][date_value].split()[:-1])








    