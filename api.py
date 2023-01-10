import aiohttp
import asyncio
from aiohttp import web
from elasticsearch import Elasticsearch

# Создаем экземпляр Elasticsearch
es = Elasticsearch(hosts=["http://localhost:9200"])


async def count(request):
    # Получаем параметры from и to из query string
    from_param = request.rel_url.query.get('from')
    to_param = request.rel_url.query.get('to')

    # Формируем запрос к Elasticsearch
    body = {
        "query": {
            "range": {
                "@timestamp": {
                    "gte": from_param,
                    "lte": to_param
                }
            }
        }
    }
    # Отправляем запрос в Elasticsearch и получаем результат
    res = es.count(index='test', doc_type='doc', body=body)

    # Формируем ответ API
    return web.json_response(res)


async def mean(request):
    # Получаем параметры from и to из query string
    from_param = request.rel_url.query.get('from')
    to_param = request.rel_url.query.get('to')

    # Формируем запрос к Elasticsearch
    body = {
        "query": {
            "range": {
                "@timestamp": {
                    "gte": from_param,
                    "lte": to_param
                }
            }
        },
        "aggs": {
            "mean_value": {
                "avg": {
                    "field": "value"
                }
            }
        }
    }
    # Отправляем запрос в Elasticsearch и получаем результат
    res = es.search(index='test', doc_type='doc', body=body)

    # Формируем ответ API
    return web.json_response(res['aggregations']['mean_value'])


async def max(request):
    # Получаем параметры from и to из query string
    from_param = request.rel_url.query.get('from')
    to_param = request.rel_url.query.get('to')

    # Формируем запрос к Elasticsearch
    body = {
        "query": {
            "range": {
                "@timestamp": {
                    "gte": from_param,
                    "lte": to_param
                }
            }
        },
        "aggs": {
            "max_value": {
                "max": {
                    "field": "value"
                }
            }
        }
    }
    # Отправляем запрос в Elasticsearch и получаем результат
    res = es.search(index='test', doc_type='doc', body=body)

    # Формируем ответ API
    return web.json_response(res['aggregations']['max_value'])


async def init_app():
    app = web.Application()
    app.router.add_get('/count', count)
    app.router.add_get('/mean', mean)
    app.router.add_get('/max', max)
    return app

app = init_app()
web.run_app(app)
