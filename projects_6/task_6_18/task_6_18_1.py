import psycopg2
import pandas as pd

try:
    connection = psycopg2.connect(
        host="localhost",          
        port="5435",               
        user="postgres",          
        password="student",       
        database="student_task"        
    )
    print("✓ Подключение установлено")

    df = pd.read_sql("SELECT * FROM products;", connection)
    print('===== Таблица products =====')
    print(df)

except Exception as error:
    print(f"Ошибка при подключении: {error}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("\n✓ Соединение с СУБД успешно закрыто.")



