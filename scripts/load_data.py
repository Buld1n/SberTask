import json
from datetime import datetime
from elasticsearch import Elasticsearch

# Инициализируем клиент Elasticsearch, указывая адрес сервера
es = Elasticsearch(hosts=["http://localhost:9200"])

# Открываем файл test.json
with open("test.json", "r") as f:
    # Загружаем данные из файла в переменную
    data = json.load(f)
    # Итерируемся по данным
    for d in data:
        # Конвертируем поле @timestamp в нужный формат
        d["@timestamp"] = datetime.strptime(d["@timestamp"], "%Y-%m-%d").isoformat()
        # Отправляем данные в Elasticsearch с помощью метода index
        es.index(index='my_index', body=d, id=d["@timestamp"])

# Закрываеи файл
f.close()
