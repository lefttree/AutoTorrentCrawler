# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TorrentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    size = scrapy.Field()
    sizeType = scrapy.Field()
    age = scrapy.Field()
    seed = scrapy.Field()
    leech = scrapy.Field()
    torrent = scrapy.Field()
    pass
