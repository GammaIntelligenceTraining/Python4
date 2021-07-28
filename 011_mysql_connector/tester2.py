import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='testdb'
)
df = pd.read_sql_query('SELECT country_or_region, score FROM happiness', mydb)
print(df['country_or_region'])