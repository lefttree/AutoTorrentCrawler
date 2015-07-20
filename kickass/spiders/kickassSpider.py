# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.utils.response import get_base_url

from kickass.items import TorrentItem


class KickassspiderSpider(scrapy.Spider):
    name = "kickass"
    allowed_domains = ["kickass.to"]
    start_urls = (
        'http://www.kickass.to/',
    )

    def __init__(self, *args, **kwargs):
        super(KickassspiderSpider, self).__init__(*args, **kwargs)
        self.keywords = kwargs['keywords'].split(',')
        self.category = kwargs['category']
        self.start_urls = [
            'http://kickass.to/usearch/category%3A'
            + self.category
            + '/?field=time_add&sorder=desc'
        ]

    def parse(self, response):
        entries = response.xpath('//tr[starts-with(@id, "torrent")]')
        items = []
        for entry in entries:
            item = TorrentItem()
            item['title'] = entry.xpath('td[1]/div[2]/div[1]/a[1]/text()').extract()
            item['url'] = entry.xpath('td[1]/div[2]/a[2]/@href').extract()
            item['torrent'] = entry.xpath('td[1]/div[1]/a[starts-with(@title, "Download torrent file")]/@href').extract()
            item['size'] = entry.xpath('td[2]/text()').extract()
            item['sizeType'] = entry.xpath('td[2]/span/text()').extract()
            item['age'] = entry.xpath('td[4]/text()').extract()
            item['seed'] = entry.xpath('td[5]/text()').extract()
            item['leech'] = entry.xpath('td[6]/text()').extract()
            
            for s in self.keywords:
                if s.lower() in item['title'][0].lower():
                    items.append(item)
                    print item
                    break
        return items
