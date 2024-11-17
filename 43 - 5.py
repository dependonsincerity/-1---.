from bs4 import BeautifulSoup
import pandas as pd

# Открываем HTML-файл
file_path = "C:/Users/klimo/Desktop/engineering/fifth_task.html"
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Парсинг HTML
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')  # Находим таблицу

# Извлечение данных из таблицы
headers = [header.get_text(strip=True) for header in table.find_all('th')]
rows = []
for row in table.find_all('tr')[1:]:
    cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
    rows.append(cells)

# Создание DataFrame
df = pd.DataFrame(rows, columns=headers)

# Сохранение в CSV с правильным разделителем
output_csv_path = "C:/Users/klimo/Desktop/engineering/rezults/fifth_complete.csv"
df.to_csv(output_csv_path, index=False, encoding='utf-8-sig', sep=';')

print(f"Данные успешно сохранены в {output_csv_path}")
