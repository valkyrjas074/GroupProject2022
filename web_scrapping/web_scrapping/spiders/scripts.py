import scrapy 
class scriptSpider(scrapy.Spider):
    name = 'script'
    start_urls = ['https://dttg.baotainguyenmoitruong.vn/chat-luong-nuoc-song-hong-nam-trong-tieu-chuan-cho-phep-242961.html']

    def parse(self, response):
        title = response.css('title::text').extract()
        post = response.css('div::text').extract()
        yield { 'title': title, 
                'main': post}