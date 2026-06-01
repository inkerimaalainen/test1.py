import numpy as np
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
    
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
connection = None



try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )

    print("✓ Подключение установлено")

    # ============================================
    # Основной датасет
    # ============================================

    df = pd.read_sql("""
    SELECT
        p.name,
        p.category,
        pr.price,
        pr.created_at
    FROM products p
    JOIN prices pr
        ON p.id = pr.product_id
    """, connection)

    # ============================================
    # Средняя цена по категориям
    # ============================================

    avg_prices = pd.read_sql("""
    SELECT
        p.category,
        AVG(pr.price) AS avg_price
    FROM products p
    JOIN prices pr
        ON p.id = pr.product_id
    GROUP BY p.category
    ORDER BY avg_price DESC
    """, connection)

    # ============================================
    # Количество товаров по категориям
    # ============================================

    products_count = pd.read_sql("""
    SELECT
        category,
        COUNT(*) AS products_count
    FROM products
    GROUP BY category
    ORDER BY products_count DESC
    """, connection)

    # ============================================
    # Топ-10 дорогих товаров
    # ============================================

    top_products = pd.read_sql("""
    SELECT
        p.name,
        AVG(pr.price) AS avg_price
    FROM products p
    JOIN prices pr
        ON p.id = pr.product_id
    GROUP BY p.id, p.name
    ORDER BY avg_price DESC
    LIMIT 10
    """, connection)

    # ============================================
    # Количество поставщиков по категориям
    # ============================================

    suppliers_count = pd.read_sql("""
    SELECT
        p.category,
        COUNT(DISTINCT s.name) AS suppliers_count
    FROM products p
    LEFT JOIN suppliers s
        ON p.id = s.product_id
    GROUP BY p.category
    ORDER BY suppliers_count DESC
    """, connection)

    # ============================================
    # Поиск аномалий
    # ============================================

    Q1 = df["price"].quantile(0.25)
    Q3 = df["price"].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[
        (df["price"] < lower) |
        (df["price"] > upper)
    ]



    category_sales = pd.read_sql("""
    SELECT
        p.category,
        SUM(pr.price) AS total_price
    FROM products p
    JOIN prices pr
        ON p.id = pr.product_id
    GROUP BY p.category
    ORDER BY total_price DESC
""", connection)
    

    # ============================================
    # ГРАФИКИ
    # ============================================

    fig, axes = plt.subplots(2, 2, figsize=(16, 9))

    # --------------------------------------------
    # 1. Средняя цена по категориям
    # --------------------------------------------

    bars = axes[0, 0].bar(
        avg_prices["category"],
        avg_prices["avg_price"]
    )

    overall_avg = avg_prices["avg_price"].mean()

    axes[0, 0].axhline(
        overall_avg,
        color='red',
        linestyle='--',
        label=f'Среднее: {overall_avg:.0f}'
                )

    for bar in bars:
        height = bar.get_height()

        axes[0, 0].text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.0f}",
            ha='center'
        )

    axes[0, 0].set_title("Средняя цена по категориям")
    axes[0, 0].set_ylabel("Цена")
    axes[0, 0].tick_params(axis='x')
    axes[0, 0].legend()

    # --------------------------------------------
    # 2. Гистограмма распределения цен
    # --------------------------------------------

    axes[0, 1].hist(
        df["price"],
        bins=15
    )

    mean_price = df["price"].mean()
    median_price = df["price"].median()

    axes[0, 1].axvline(
        mean_price,
        color='green',
        linestyle='--',
        label=f'Среднее: {mean_price:.0f}'
    )

    axes[0, 1].axvline(
        median_price,
        color='red',
        linestyle=':',
        label=f'Медиана: {median_price:.0f}'
    )

    axes[0, 1].set_title("Распределение цен")
    axes[0, 1].set_xlabel("Цена")
    axes[0, 1].set_ylabel("Количество товаров")
    axes[0, 1].legend()

    axes[0, 1].text(
        0.98,
        0.95,
        f"Всего записей: {len(df)}",
        transform=axes[0, 1].transAxes,
        ha='right',
        va='top',
        bbox=dict(boxstyle="round")
    )
    axes[0, 1].annotate(
    f"Выбросы начинаются с {upper:.0f}",
    xy=(upper, 1),          # куда указывает стрелка
    xytext=(upper * 1.15, 8),  # где расположен текст
    arrowprops=dict(
        arrowstyle="->",
        lw=2
    ),
    bbox=dict(
        boxstyle="round",
        facecolor="lightyellow"
    )
)

    # --------------------------------------------
    # 3. Boxplot цен по категориям
    # --------------------------------------------

    sns.boxplot(
    data=df,
    x="category",
    y="price",
    palette="Set2",
    showfliers=True,
    ax=axes[1, 0]
)

    sns.stripplot(
    data=df,
    x="category",
    y="price",
    hue="category",
    palette="Set2",
    jitter=0.2,
    alpha=0.5,
    size=5,
    legend = False,
    ax=axes[1, 0]
)
    axes[1, 0].set_ylabel("Цена")
    axes[1, 0].set_xlabel("Категория")


# --------------------------------------------
# 4. Круговая диаграмма товаров по категориям
# --------------------------------------------

    axes[1, 1].pie(
    category_sales["total_price"],
    labels=category_sales["category"],
    autopct='%1.1f%%',
    startangle=90
)

    axes[1, 1].set_title(
    "Доля категорий в общей стоимости товаров"
)
    plt.tight_layout()
    plt.show()
    # ============================================
    # Выводы
    # ============================================

    print("\n========== ВЫВОДЫ ==========")

    print(
        f"\nСамая дорогая категория: "
        f"{avg_prices.iloc[0]['category']}"
    )

    print(
        f"Средняя цена по всем категориям: "
        f"{overall_avg:.2f}"
    )

    print(
        f"Обнаружено аномалий: "
        f"{len(outliers)}"
    )

    if len(outliers) > 0:
        print("\nПримеры аномальных цен:")
        print(outliers[["name", "price"]].head())

    else:
        print("\nАномалии не обнаружены")

except Exception as error:
    print("Ошибка:", error)

finally:
    if connection:
        connection.close()
        print("\n✓ Соединение закрыто")