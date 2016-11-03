# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlRelatedChannelsPipeline(object):

    def open_spider(self, spider):
        self.file = open('url.txt', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        url = item['channel_url'] + '/videos' + '\n'
        self.file.write(url)
        return item