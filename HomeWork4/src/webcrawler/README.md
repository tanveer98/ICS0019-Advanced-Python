# A webscraper for osta.ee written with python and scrapy

## dependencies
You need python package `scrapy` to run this crawler

## To run:

just run the main.py script. It will scrape the computers section of osta.ee scrape the data, and store it in data/computers.json file.


## Directory structure:

#### Root directory:
* settings.py:\
	Main script to run the crawler.


#### Webcrawler module
* settings.py:\
	contains all the necessary settings for the crawler, i.e json output file name, output formatting.
	This file also contains configuartion of the auto throttler. Disable auto throttles from settings.py for maximum performance
	(With current configuartion, the crawler's throughput is roughly 20-30 pages a minute.
	So to scrape the entire computers section will require roughly 6-7 minutes)
* spiders/osta.py:\
	Contains OstaSpider class definition. scrapy instantiates this class to scrape the target website (osta.ee)

