import requests
from bs4 import BeautifulSoup

# Получение данных из API
url = "https://dummyjson.com/products"
response = requests.get(url)
data = response.json()

# Преобразование данных в HTML-таблицу
products = data['products']
html_table = """
<table border="1">
    <tr>
        <th>Title</th>
        <th>Category</th>
        <th>Price</th>
        <th>Stock</th>
    </tr>
"""
for product in products:
    html_table += f"""
    <tr>
        <td>{product['title']}</td>
        <td>{product['category']}</td>
        <td>{product['price']}</td>
        <td>{product['stock']}</td>
    </tr>
    """
html_table += "</table>"

# Сохранение в HTML файл
with open("six.html", "w", encoding="utf-8") as file:
    file.write(html_table)

print("Данные сохранены в 'six.html'")
