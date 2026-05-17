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

    cat_stat = df.groupby('product_category')['price'].agg(
        count='count',       
        mean='mean',         
        median='median',     
        std='std'           
    )

    cat_stat_sort = cat_stat.sort_values(by='mean', ascending=False)

    print("\n=================== анализ цен по категориям товаров ===================")
    
    cat_stat_sort.columns = ['Кол-во цен', 'Средняя цена', 'Медиана', 'Ст. отклонение']
    
    print(cat_stat_sort.round(2).to_string())
    print("========================================================================")


except Exception as error:
    print(f"Ошибка при подключении: {error}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("\n✓ Соединение с СУБД успешно закрыто.")