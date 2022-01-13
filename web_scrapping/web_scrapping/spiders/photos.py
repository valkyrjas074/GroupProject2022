import scrapy

class PhotosSpider(scrapy.Spider):
    name = 'photos'
    url_src = input("Link:")
    start_urls = [url_src] 

    def parse(self, response):
        raw_image_urls = response.css('.image img ::attr(src)').getall()
        clean_image_urls=[]
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        
        yield {
            'image_urls': clean_image_urls
        }

