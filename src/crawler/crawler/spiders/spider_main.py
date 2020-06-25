from crawler.items import CrawlerItem
import scrapy
import time


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = []
    start_urls = ['https://udn.com/news/story/120775/4112519']

    def parse(self, response):
        time.sleep(1)
        item = CrawlerItem()
        try:
            item['content'] = response.css('p::text').extract()
            yield item
        except IndexError:
            pass
