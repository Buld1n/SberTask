import unittest
import requests


class TestAPI(unittest.TestCase):
    def test_count(self):
        # Отправляем GET запрос на метод count
        response = requests.get('http://localhost:8080/count?from=2022-01-01T00:00:00&to=2022-12-31T23:59:59')
        # Проверяем, что ответ корректный
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['count'], int)

    def test_mean(self):
        # Отправляем GET запрос на метод mean
        response = requests.get('http://localhost:8080/mean?from=2022-01-01T00:00:00&to=2022-12-31T23:59:59')
        # Проверяем, что ответ корректный
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['value'], float)

    def test_max(self):
        # Отправляем GET запрос на метод max
        response = requests.get('http://localhost:8080/max?from=2022-01-01T00:00:00&to=2022-12-31T23:59:59')
        # Проверяем, что ответ корректный
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['value'], float)


if __name__ == '__main__':
    unittest.main()
