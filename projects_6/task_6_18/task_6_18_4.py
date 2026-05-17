import psycopg2
import pandas as pd

try:
    connection = psycopg2.connect(
        host='localhost',          
        port='5435',              
        user='postgres',           
        password='student',        
        database='student_task'         
    )
    print('✓ Подключение установлено')


    query = '''
    SELECT 
        pr.id AS price_id,
        p.name AS product_name,
        p.category AS product_category,
        pr.price,
        pr.created_at
    FROM prices pr
    JOIN products p ON pr.product_id = p.id
    ORDER BY pr.id;
    '''
    df = pd.read_sql(query, connection)

    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50) 
    q3 = df['price'].quantile(0.75)
    
    iqr = q3 - q1

    print('\n' + '='*50)
    print(' ' * 15 + 'Расчёт квартилей и IQR' + ' ' * 15)
    print('='*50)
    print(f'Первый квартиль (Q1, 25%)      : {q1:.2f} руб.')
    print(f'Второй квартиль (Q2, Медиана)  : {q2:.2f} руб.')
    print(f'Третий квартиль (Q3, 75%)      : {q3:.2f} руб.')
    print(f'Межквартильный размах (IQR)    : {iqr:.2f} руб.')
    print('='*50)

    expensive_products = df[df['price'] > q3]

    print(f'\n=== Список товаров дороже Q3 (Всего найдено: {len(expensive_products)}) ===')
    
    premium_list = expensive_products[['product_name', 'product_category', 'price']].drop_duplicates(subset=['product_name'])
    
    print(premium_list.to_string(index=False, formatters={'price': '{:.2f} руб.'.format}))


except Exception as error:
    print(f'Ошибка при подключении: {error}')
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print('\n✓ Соединение с СУБД успешно закрыто.')