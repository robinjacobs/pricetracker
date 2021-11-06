import scrapy

# custom library
import time
import re
import os.path


class PriceSpider(scrapy.Spider):
    name = 'prices'

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        url_file_name = 'price_urls.txt'

        if not os.path.exists(url_file_name) :
            raise FileNotFoundError

        with open(url_file_name) as f :
            self.urls = f.readlines()

        self.log(f"Found the following URLs to track : {self.urls}")

    def start_requests(self) :
        urls = ['']
        for url in self.urls :
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'prices-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        
        filename = 'current-prices.csv'
        price_raw = response.xpath('/html/body/div/div/div/div[1]/main/div/div/div[2]/div/div[2]/div/div[1]/span/strong/text()').get()
        product_name = response.xpath('//*[@id="pageContent"]/div/div/div[2]/div/div[2]/div/h1/span/').get()
        
        
        self.log(str(type(price_raw)))
        self.log(product_name)

        pricels = price_raw.split('.')
        price = pricels[0]

        self.log(str(pricels))
        self.log(f'price : {price} ')
        
        with open(filename, 'a') as f:
            f.write(str(time.time()) + ',' + product_name  + ',' + str(price) + '\n')
        
        print(price)


