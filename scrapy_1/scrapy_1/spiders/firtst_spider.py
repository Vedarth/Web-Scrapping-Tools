import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://query.nytimes.com/search/sitesearch/#/microsoft/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open('scrap.txt', 'wb') as f:
            f.write(response.body)