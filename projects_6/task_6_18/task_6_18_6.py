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



    price_range = df.groupby(['product_name', 'product_category'])['price'].agg(
        min_price='min',
        max_price='max'
    ).reset_index()

    price_range['price_difference'] = price_range['max_price'] - price_range['min_price']

    spread = price_range.sort_values(by='price_difference', ascending=False)

    print("\n================================== Разброс цен =================================")
    
    spread.columns = ['Название товара', 'Категория', 'Мин. цена', 'Макс. цена', 'Разница (разброс)']
    
    print(spread.round(2).to_string(index=False, formatters={
        'Мин. цена': '{:.2f} руб.'.format,
        'Макс. цена': '{:.2f} руб.'.format,
        'Разница (разброс)': '{:.2f} руб.'.format
    }))
    print("==================================================================================")


except Exception as error:
    print(f"Ошибка при подключении: {error}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("\n✓ Соединение с СУБД успешно закрыто.")