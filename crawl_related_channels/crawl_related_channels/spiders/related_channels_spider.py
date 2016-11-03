import scrapy
youtube_url = 'https://www.youtube.com'


class RelatedChannelsSpider(scrapy.Spider):
    name = 'related_channel_spider'

    def start_requests(self):
        start_urls = [{
            'url': 'https://www.youtube.com/user/BigRigTravels/featured',
            'title': 'BigRigTravels Video Vault'
        }]
        for url in start_urls:
            request = scrapy.Request(url['url'], callback=self.parse)
            request.meta['title'] = url['title']
            yield request

    def parse(self, response):
        meta = response.meta
        channel_title = meta['title']
        channel_url = response.url
        yield {
            'channel_title': channel_title,
            'channel_url': channel_url
        }
        channel_item_lis = response.xpath('//li[contains(@class, "branded-page-related-channels-item")]')
        for channel_item_li in channel_item_lis:
            next_channel_title = channel_item_li.xpath('span/div[contains(@class, "yt-lockup-content")]/h3/a/text()').extract()[0]
            relative_url = channel_item_li.xpath('span/div[contains(@class, "yt-lockup-content")]/h3/a/@href').extract()[0]
            next_channel_url = youtube_url + relative_url
            request = scrapy.Request(next_channel_url, callback=self.parse)
            request.meta['title'] = next_channel_title
            yield request

