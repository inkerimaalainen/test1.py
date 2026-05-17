import psycopg2
import pandas as pd

try:
    #1. Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",          # База в контейнере, но доступна через localhost
        port="5435",               # Порт из секции ports
        user="postgres",           # POSTGRES_USER
        password="student",        # POSTGRES_PASSWORD
        database="student_task"          # POSTGRES_DB
    )
    print("✓ Подключение установлено")



    # 2. SQL запрос с JOIN
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
    print('===== Статистика по ценам товаров =====')
    print(f"Средняя цена: {df['price'].mean()} руб.")
    print(f"Медиана: {df['price'].median()} руб.")
    print(f"Стандартное отклонение: {df['price'].std()} руб.")
    print(f"Минимальная цена: {df['price'].min()} руб.")
    print(f"Максимальная цена: {df['price'].max()} руб.")

except Exception as error:
    print(f"Ошибка при подключении: {error}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("\n✓ Соединение с СУБД успешно закрыто.")