import scrapy
from productscraper.items import ProductscraperItem 
from scrapy_selenium import SeleniumRequest

class MouseSpider(scrapy.Spider):
    name = 'mouse'
    allowed_domains = ['www.lazada.com.ph']
    start_urls = ['https://www.lazada.com.ph/shop-gaming-mice/logitech/']

    url = 'https://www.lazada.com.ph/shop-gaming-mice/logitech/'

    splash_script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(3))
            assert(splash:set_viewport_full())
            assert(splash:wait(3))
            return {
                html = splash:html(),
                }
        end
        
    '''

    def start_requests(self):

        yield SeleniumRequest(url='https://www.lazada.com.ph/shop-gaming-mice/logitech/', callback=self.parse, script='window.scrollTo(0, document.body.scrollHeight);')
        # yield SplashRequest(url='https://www.lazada.com.ph/shop-gaming-mice/logitech/', callback=self.parse, endpoint='execute', args={'lua_source': self.splash_script})
 
    def parse(self, response):
        
        print(response)

        #Product is the div of each product 'card' in results page
        products = response.xpath("//div[contains(@data-qa-locator, 'product-item')]/div[contains(@class, 'c3e8SH c2mzns')]")

        for product in products:
            item = ProductscraperItem()
            item['name'] = product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'c16H9d')]/a/text()").get()
            item['url'] = product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'c16H9d')]/a/@href").get()
            item['price'] = product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'c3gUW0')]/span/text()").get()
            item['img_src'] = product.xpath("./div[contains(@class, 'c5TXIP')]//div[contains(@class, 'cRjKsc')]/a/img/@src").get()
            yield item
