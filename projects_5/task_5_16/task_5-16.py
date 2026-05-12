# -*- coding: utf-8 -*-
import psycopg2
import sys

# Устанавливаем кодировку потока вывода
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5434",
        user="postgres",
        password="example",
        database="testdb",
        client_encoding="UTF8"
    )
    
    cursor = connection.cursor()
    
    # Очищаем таблицу перед вставкой (с каскадным удалением)
    cursor.execute("TRUNCATE TABLE students CASCADE")
    
    # Вставляем данные (используем существующие колонки)
    cursor.execute("""
        INSERT INTO students (first_name, last_name) VALUES
        ('Иван', 'Петров'),
        ('Мария', 'Сидорова'),
        ('Алексей', 'Иванов')
    """)
    connection.commit()
    
    # Выполняем SELECT запрос
    cursor.execute("SELECT * FROM students ORDER BY student_id")
    
    # Получаем результаты
    students = cursor.fetchall()
    
    print("=" * 60)
    print("Результаты запроса - Студенты:")
    print("=" * 60)
    for student in students:
        print(student)
    print("=" * 60)
    print(f"Всего студентов: {len(students)}")

except psycopg2.OperationalError as error:
    print(f"Ошибка подключения: {error}")
except Exception as error:
    if connection:
        connection.rollback()
    print(f"Ошибка: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
    print("Подключение закрыто.")
