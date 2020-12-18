# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging



class ProductscraperPipeline:
        
        def __init__(self):
            self.connection = pymongo.MongoClient(
                "localhost", 
                27017 )
            db = self.connection["scraped_products"]
            self.collection = db["logitech_mice"]


        def process_item(self, item, spider):
            
            self.collection.insert(dict(item))
            return item