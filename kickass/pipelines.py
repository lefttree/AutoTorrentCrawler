# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
Typical use for item pipelines are:

    cleansing HTML data
    validating scraped data (checking that the items contain certain fields)
    checking for duplicates (and dropping them)
    storing the scraped item in a database
'''

import json
import subprocess
import time
import urllib2


class KickassPipeline(object):
    def process_item(self, item, spider):
        return item

class TorrentPipeline(object):
    def process_item(self, item, spider):
        print "Downloading " + item['title'][0]
        path = item['torrent'][0]
        subprocess.call(['kickass/curl_torrent.sh', path])
        time.sleep(10)
        return item
