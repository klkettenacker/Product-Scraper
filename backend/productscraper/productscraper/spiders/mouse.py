import scrapy
import requests
from scrapy_splash import SplashRequest

class MouseSpider(scrapy.Spider):
    name = 'mouse'
    start_urls = ['https://www.lazada.com.ph/shop-gaming-mice/logitech/']

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(3))
            return {
                html = splash:html(),
                }
        end
        
    '''

    def start_requests(self):
        yield SplashRequest(url='https://www.lazada.com.ph/shop-gaming-mice/logitech/', callback=self.parse, endpoint='execute', args={'lua_source': self.script})
 
    def parse(self, response):
        print(response.body)

        products = response.xpath("//div[contains(@data-qa-locator, 'product-item')]/div[contains(@class, 'c3e8SH c2mzns')]")

        for product in products:
            yield {
                'product-name': product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'c16H9d')]/a/text()").get(),
                'product-link': product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'c16H9d')]/a/@href").get(),
                'product-price': product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'c3gUW0')]/span/text()").get(),
                'product-image': product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'cRjKsc')]/a/img/@src").get()
                
            }

