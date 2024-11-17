import pandas as pd

# Укажите путь к исходному файлу
file_path = 'C:/Users/klimo/Desktop/engineering/fourth_task.txt'
data = pd.read_csv(file_path, delimiter=",")

# Удаление из таблицы столбец 'rating'
data_modified = data.drop(columns=['rating'])

# Среднее, максимум и минимум по столбцу 'price'
price_mean = data['price'].mean()
price_max = data['price'].max()
price_min = data['price'].min()

# Отфильтр строк, где category не равна 'Бакалея'
filtered_data = data_modified[data_modified['category'] != 'Бакалея']

# Возврат рехультатов в текстовый файл
results_path = 'C:/Users/klimo/Desktop/engineering/results_values.txt'
with open(results_path, 'w', encoding='utf-8') as results_file:
    results_file.write(f"{price_mean}\n{price_max}\n{price_min}")

# Сохранение таблицы
filtered_csv_path = 'C:/Users/klimo/Desktop/engineering/rezults/fourth_complete.csv'
filtered_data.to_csv(filtered_csv_path, index=False, encoding='utf-8')

print(f"Результаты сохранены:\n- Средние, максимум и минимум: {results_path}\n- Модифицированная таблица: {filtered_csv_path}")
