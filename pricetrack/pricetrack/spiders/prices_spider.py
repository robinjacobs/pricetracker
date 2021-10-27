import scrapy
import time

class PriceSpider(scrapy.Spider):
    name = 'prices'

    def start_requests(self) :
        urls = ['']
        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'prices-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        
        filename = 'current-prices.csv'
        price = response.xpath('/html/body/div/div/div/div[1]/main/div/div/div[2]/div/div[2]/div/div[1]/span/strong/text()').get()
        
        self.log(f'price : {price} ')
        
        with open(filename, 'a') as f:
            f.write(str(price)+"\n")
        
        print(price)


