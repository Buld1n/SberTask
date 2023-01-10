import requests

# Проверяем метод count
response = requests.get('http://localhost:8080/count?from=2022-01-01T00:00:00&to=2022-12-31T23:59:59')
print(response.json())

# Проверяем метод mean
response = requests.get('http://localhost:8080/mean?from=2022-01-01T00:00:00&to=2022-12-31T23:59:59')
print(response.json())

# Проверяем метод max
response = requests.get('http://localhost:8080/max?from=2022-01-01T00:00:00&to=2022-12-31T23:59:59')
print(response.json())
