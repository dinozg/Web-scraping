# quote_spider_follow_links.py file

from scrapy import Spider, Request

class QuoteSpiderFollowLinks(Spider):
    # unique identifier of this spider
    name = "quotes_follow_links"
    # start_urls for url list to crawl automatically
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    # callback method to handle responses
    def parse(self, response):
        # get the div elements with class name quote
        for quote in response.css('div.quote'):
            # yield a quote dictionary
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        # get next page element via the href attribute
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # create the next page url
            next_page = response.urljoin(next_page)
            # request the next page with Scrapy Request
            yield Request(next_page, callback=self.parse)


####  respnse.follow()  ###
class QuoteSpiderFollowLinks(Spider):
    # unique identifier of this spider
    name = "quotes_follow_links"
    # start_urls for url list to crawl automatically
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    # callback method to handle responses
    def parse(self, response):
        # get the div elements with class name quote
        for quote in response.css('div.quote'):
            # yield a quote dictionary
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        # get next page element via the href attribute
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # yield a Request object with response.follow()
            yield response.follow(next_page, callback=self.parse)


