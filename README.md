# AutoTorrentCrawler
Torrent crawler to get bit torrent from kickass.io and start uTorrent to automatically download

###About

In this project, I have written a Scrapy crawler that uses the get bit torrent from kickass.io and start uTorrent to download 
any resource automatically. 
This project demonstrates familiarity with:

1. Scrapy 

2. Python, Shell script 

3. HTML DOM, xPath selector


Requirements:

1. Python >= 2.7 

2. [Scrap](http://doc.scrapy.org/en/latest/intro/install.html#installing-scrapy)

3. Curl

4. [btc](https://github.com/bittorrent/btc)

### Files 

```
├── LICENSE
├── kickass
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── curl_torrent.sh
│   ├── items.py
│   ├── items.pyc
│   ├── pipelines.py
│   ├── pipelines.pyc
│   ├── settings.py
│   ├── settings.pyc
│   └── spiders
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── g.py
│       ├── g.pyc
│       ├── kickassSpider.py
│       └── kickassSpider.pyc
└── scrapy.cfg
```

### Usage

1. Install python, scrapy, btc and curl on your computer

2. Run crawler 

```
scrapy crawl -a keywords="<keyword>, <keyword>" -a category="<category>"
```

For example

`scrapy crawl -a keywords="man" -a category="movies"`

### License 

MIT
