import csv
import configparser
import datetime
import mysql.connector as connection
import pandas as pd

try:
    parser = configparser.ConfigParser()
    parser.read("pipeline.conf")

    database = parser.get("mysql_config", "database")
    user = parser.get("mysql__config", "username")
    password = parser.get("mysql__config", "password")
    host = parser.get("mysql__config", "host")

    conn_str = f"host={host}, database={database}, user={user}, passwd={password},use_pure=True"
    conn = connection.connect(conn_str)
    
    DATA_FOLDER = "data"
    
    tables = [
    "addresses",
    "order_items",
    "products",
    "promos",
]
    for table in tables:
   
   
        query = "Select * from table;"
    
    result_dataFrame = pd.read_sql(query,mydb)
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))

