# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class ProductscraperItem(Item):
    name = Field()
    url = Field()
    price = Field()
    img_src = Field()