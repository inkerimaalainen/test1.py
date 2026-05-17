import psycopg2
import pandas as pd

# 1. Подключаемся к базе
connection = psycopg2.connect(
    host="localhost",         
    port="5435",               
    user="postgres",           
    password="student",        
    database="student_task"    
)

my_sql_query = """
SELECT p.name, pr.price 
FROM products p
JOIN prices pr ON p.id = pr.product_id
LIMIT 5;
"""

df = pd.read_sql(my_sql_query, connection)
print(df)

connection.close()