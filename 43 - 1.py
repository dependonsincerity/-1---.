# Загружаем текст и разбиваем его на слова, как и в первой части
file_path = r'C:\Users\klimo\Desktop\engineering\first_task.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()  # Разбиваем текст на слова

# Подсчитываем количество и долю коротких слов длиной от 1 до 5 символов
total_words = len(words)
short_words_count = sum(1 for word in words if 1 <= len(word) <= 5)
short_words_ratio = short_words_count / total_words

# Подготавливаем результат для вывода в файле статистики коротких слов
variant_result_text = f"{short_words_count}\n{short_words_ratio:.4f}"

# Укажите путь для сохранения результата статистики коротких слов
variant_output_file_path = r'C:\Users\klimo\Desktop\engineering\rezults\first_complete.txt'
with open(variant_output_file_path, 'w', encoding='utf-8') as variant_output_file:
    variant_output_file.write(variant_result_text)

print("Файл с результатами коротких слов сохранен по адресу:", variant_output_file_path)
