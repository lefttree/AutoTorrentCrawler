# -*- coding: utf-8 -*-
import scrapy


class GSpider(scrapy.Spider):
    name = "g"
    allowed_domains = ["www.google.com"]
    start_urls = (
        'http://www.www.google.com/',
    )

    def parse(self, response):
        pass
