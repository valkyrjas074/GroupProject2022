import scrapy 
from scrapy.crawler import CrawlerProcess
class ScriptSpider(scrapy.Spider):
    name = 'script'

    def startRequest(self):
        yield (scrapy.Request('https://blog.coinbase.com/coinbase-and-mastercard-partner-to-revolutionize-nft-purchase-experience-8e486a392c55'))
   

    def parse(self, response):
        title = response.css('title::text').extract()
        yield { 'title': title}
    

process = CrawlerProcess(settings = {
        'FEED_URI': 'script.json',
        'FEED_FORMAT': 'json'
    })

process.crawl(ScriptSpider)
process.start()

