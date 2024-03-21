# quote_spider_extractor.py file

from scrapy import Spider, Request

class QuoteSpiderExtractor(Spider):
    # unique identifier of this spider
    name = "quotes_extractor"
    # start_urls for url list to crawl automatically
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    # callback method to handle responses
    def parse(self, response):
        # get the div elements with class name quote
        for quote in response.css('div.quote'):
            # yield a quote dictionary
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }


