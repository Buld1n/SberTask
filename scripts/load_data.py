# Импортируем библиотеку elasticsearch
from elasticsearch import Elasticsearch
# Импортируем библиотеку json
import json

# Инициализируем клиент Elasticsearch, указывая адрес сервера
es = Elasticsearch(hosts=["http://localhost:9200"])

# Открываем файл test.json
with open("test.json", "r") as f:
    # Загружаем данные из файла в переменную
    data = json.load(f)
    # Итерируемся по данным
    for d in data:
        # Отправляем данные в Elasticsearch с помощью метода index
        es.index(index='my_index', document=data)

# Закрываеи файл
f.close()
