# Укажите путь к исходному файлу
test_file_path = r'C:\Users\klimo\Desktop\engineering\second_task.txt'

# Открытие и чтение содержимого исходного файла
with open(test_file_path, 'r', encoding='utf-8') as test_file:
    lines = test_file.readlines()

# Обработка каждой строки в соответствии с заданной операцией:
# Суммируем только абсолютные значения чисел, квадрат которых не превышает 100000
row_sums = []
for line in lines:
    numbers = map(int, line.split())  # Преобразуем числа в строке в целые числа
    filtered_sum = sum(abs(num) for num in numbers if num ** 2 <= 100_000)  # Суммируем, если квадрат числа <= 100000
    row_sums.append(filtered_sum)

# Сортировка сумм по убыванию и выборка топ-10 сумм
top_10_sums = sorted(row_sums, reverse=True)[:10]

# Форматирование результата в строку
top_10_result_text = "\n".join(map(str, top_10_sums))

# Укажите путь для сохранения выходного файла
top_10_output_file_path = r'C:\Users\klimo\Desktop\engineering\rezults\second_complete.txt'

# Сохранение результата в новый файл
with open(top_10_output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(top_10_result_text)

# Возвращаем путь к файлу с результатом
top_10_output_file_path
