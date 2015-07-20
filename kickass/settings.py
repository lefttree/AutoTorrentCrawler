# -*- coding: utf-8 -*-

# Scrapy settings for kickass project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kickass'

SPIDER_MODULES = ['kickass.spiders']
NEWSPIDER_MODULE = 'kickass.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kickass (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'kickass.pipelines.TorrentPipeline': 300
    }
