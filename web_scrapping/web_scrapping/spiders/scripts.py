import scrapy 
class scriptSpider(scrapy.Spider):
    name = 'script'

    input_urls = input("Urls:\n")
    start_urls = [input_urls]

    def parse(self, response):
        title = response.css('title::text').extract()
        post = response.css('div::text').extract()
        yield { 'title': title, 
                'main': post}