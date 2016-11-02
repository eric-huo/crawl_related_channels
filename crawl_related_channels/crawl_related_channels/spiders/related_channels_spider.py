import scrapy


class RelatedChannelsSpider(scrapy.Spider):
    name = 'related_channel_spider'
    start_urls = [
        'https://www.youtube.com/user/BigRigTravels/featured'
    ]

    def parse(self, response):
        pass