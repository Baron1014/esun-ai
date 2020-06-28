from crawler.items import CrawlerItem
import scrapy
import time
import pandas as pd


class NewsSpider(scrapy.Spider):
    # 讀取所有網址
    traing_csv = "../../data/raw/模型訓練資料/tbrain_train_final_0610.csv"
    df = pd.read_csv(traing_csv)

    name = 'news'
    allowed_domains = []
    start_urls = df['hyperlink'].to_list()

    def parse(self, response):
        item = CrawlerItem()
        time.sleep(1)
        try:
            item['res'] = response
            item['news'] = response.css('p::text').extract()
            yield item
        except IndexError:
            pass
