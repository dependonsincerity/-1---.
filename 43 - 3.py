import numpy as np

# Укажите путь к файлу с данными и где сохранить результат
third_task_path = r'C:\Users\klimo\Desktop\engineering\third_task.txt'
output_file_path = r'C:\Users\klimo\Desktop\engineering\rezults\third_complete.txt'

# Чтение данных из файла
with open(third_task_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()


# Функция для замены 'N/A' на среднее значение соседних чисел
def replace_na_with_neighbors_avg(numbers):
    processed_numbers = [None if num == 'N/A' else int(num) for num in numbers]

    # Замена пропусков средним значением соседних чисел
    for i in range(1, len(processed_numbers) - 1):
        if processed_numbers[i] is None:
            left = processed_numbers[i - 1] if processed_numbers[i - 1] is not None else 0
            right = processed_numbers[i + 1] if processed_numbers[i + 1] is not None else 0
            processed_numbers[i] = (left + right) / 2

    # Обработка пропусков в начале и в конце строки
    if processed_numbers[0] is None:
        processed_numbers[0] = processed_numbers[1] if processed_numbers[1] is not None else 0
    if processed_numbers[-1] is None:
        processed_numbers[-1] = processed_numbers[-2] if processed_numbers[-2] is not None else 0

    return processed_numbers


# Обработка строк и выполнение фильтрации
row_sums = []
for line in lines:
    numbers = line.split()
    processed_numbers = replace_na_with_neighbors_avg(numbers)

    # Фильтруем только нечетные значения, не превышающие 500
    filtered_numbers = [int(num) for num in processed_numbers if int(num) % 2 != 0 and int(num) <= 500]

    # Рассчитываем сумму по каждой строке
    row_sum = sum(filtered_numbers)
    row_sums.append(row_sum)

# Запись результата в файл
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for sum_value in row_sums:
        output_file.write(f"{sum_value}\n")

print(f"Результаты сохранены в {output_file_path}")
