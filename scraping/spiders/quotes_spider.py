# quotes_spider.py file

from scrapy import Spider, Request

# class QuotesSpider(Spider):
#     # unique identifier of this spider
#     name = "quotes"
#
#     # begin crawl and return an iterable
#     def start_requests(self):
#         urls = [
#             'https://quotes.toscrape.com/page/1/',
#             'https://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield Request(url=url, callback=self.parse)
#
#     # callback method to handle responses
#     def parse(self, response):
#         # get the page number from response
#         page = response.url.split("/")[-2]
#         # create a filename as quotes-1.html
#         filename = f'quotes-{page}.html'
#         # write into this file
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         # log the activity
#         self.log(f'Saved file {filename}')


# redefine the same spider with start_urls
class QuotesSpider(Spider):
    # unique identifier of this spider
    name = "quotes"
    # start_urls for url list to crawl automatically
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    # callback method to handle responses
    def parse(self, response):
        # get the page number from response
        page = response.url.split("/")[-2]
        # create a filename as quotes-1.html
        filename = f'quotes-{page}.html'
        # write into this file
        with open(filename, 'wb') as f:
            f.write(response.body)

