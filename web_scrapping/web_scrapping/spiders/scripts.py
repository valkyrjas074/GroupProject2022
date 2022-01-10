import scrapy 
class scriptSpider(scrapy.Spider):
    name = 'script'
    start_urls = ['https://en.wikipedia.org/wiki/Christmas']

    def parse(self, response):
        title = response.css('title::text').extract()
        post = response.css('.vector-body::text').extract()
        yield { 'title': title, 
                'main': post}




    
