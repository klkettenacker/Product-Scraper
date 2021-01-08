# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import logging
import json
from scrapy.utils.serialize import ScrapyJSONEncoder

_encoder = ScrapyJSONEncoder()

global url
global headers
global data


url = 'https://api.jsonbin.io/b/5ff755d609f7c73f1b6edc6f'
headers = { 'versioning': 'false',
            'Content-Type': 'application/json',
           #'collection-id': '5fdee3bf87e11161f87ce5f4',
           'secret-Key': '$2b$10$p1MJn9niCcUaS11hWerZVOpyJz8o0vmC6Sc9sitXQmjvz4lt2iriG'}

data = []

class ProductscraperPipeline:

    def __init__(self):
        asd = 0

    def process_item(self, item, spider):
        data.append(item)
        return item


    def close_spider(self, spider):

        bruh = _encoder.encode(data)

        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

        req = requests.put(url=url, headers=headers, json=json.loads(bruh))
        print(req.text)

    