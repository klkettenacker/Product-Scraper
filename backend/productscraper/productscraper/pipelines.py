# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import logging
import json


url = 'https://api.jsonbin.io/b/5fdee52187e11161f87ce649'
headers = {'versioning': 'false', 
           'Content-Type': 'application/json',
           'secret-key': '$2b$10$p1MJn9niCcUaS11hWerZVOpyJz8o0vmC6Sc9sitXQmjvz4lt2iriG'}

data = []

class ProductscraperPipeline:
    global data

    def __init__(self):
        asd = 0

    def process_item(self, item, spider):
        data.append(item)
        return item

        if(len(data) >= 40):
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASDKLKASDJLAKSDDASKLDJAKLSDASJSD')
            print(url)
            json_data = json.dumps(data)
            req = requests.put(url=url, json=json_data, headers=headers)
            print(req.text)
