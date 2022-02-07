import scrapy
from scrapy.crawler import CrawlerProcess

class PhotosSpider(scrapy.Spider):
    name = 'photos'

    def start_requests(self):
        yield scrapy.Request('https://www.nytimes.com/')

    def parse(self, response):
        raw_image_urls = response.css('img ::attr(src)').getall()
        clean_image_urls=[]
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        
        yield {
            'image_urls': clean_image_urls
        }
        
process = CrawlerProcess(settings = {
    'FEED_URI': 'photos_url.json',
    'FEED_FORMAT': 'json'
})

process.crawl(PhotosSpider)
process.start()
