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


    query = """
    SELECT 
        pr.id AS price_id,
        p.name AS product_name,
        p.category AS product_category,
        pr.price,
        pr.created_at
    FROM prices pr
    JOIN products p ON pr.product_id = p.id
    ORDER BY pr.id;
    """

    df = pd.read_sql(query, connection)
    print(df)

except Exception as error:
    print(f"Ошибка при подключении: {error}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("\n✓ Соединение с СУБД успешно закрыто.")