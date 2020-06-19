#!/usr/bin/env python
'''
Main module to run the crawler for osta.ee
'''
from webcrawler.spiders.osta import OstaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


if __name__ == "__main__":
    PROC = CrawlerProcess(get_project_settings())
    PROC.crawl(OstaSpider)
    PROC.start()
    