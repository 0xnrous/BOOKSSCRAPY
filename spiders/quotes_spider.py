import scrapy
from ..items import BookItem

class BookSpider(scrapy.Spider):
    name ='Book'
    start_urls = [

        'https://books.toscrape.com/'

                ]
    def parse(self, response):
        items=BookItem()
        all_Book_tp=response.css('article.product_pod')
        for Book in all_Book_tp:
            title = Book.css('h3 > a::text').extract()
            price = Book.css('.price_color::text').extract()
            items['title']=title
            items['price']=price
            yield items
        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)










































































