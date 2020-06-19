# -*- coding: utf-8 -*-
'''
This module contains the definition of OstaSpider class
'''

import scrapy


class OstaSpider(scrapy.Spider):
    '''
    This class contains methods to scrape data from osta.ee
    '''

    name = 'osta'
    allowed_domains = ['osta.ee']
    start_urls = ['https://www.osta.ee/en/category/computers']

    def parse(self, response):
        '''
        Parse generator generates a dictionary containing all the scraped data from the url.
        Since url can contain an arbitrary amount of items (often thousands of items)
        it yields the collected data one by one. When it scrapes all data from one page
        it tries to get the url of next page and start scraping data from that page.
        If not, then the generator returns.

        @Param response: HTMLResponse of the start_urls
        @yield: Dictionary with 'Title', 'Price', 'Picture href'
        '''

        undorded_list = response.xpath(
            r'/html/body/div[1]/div[16]/div[1]/div/div[2]/main/div/article/ul[2]'
        )[0]
        list_items = undorded_list.css('li')

        ###############
        # First we try to scarpe all the items in the current page.
        ###############
        for l_item in list_items:

            # if list item contains a footer section, it should be a product list item.
            # Otherwise, ignore,
            footer = l_item.css('footer')
            if footer:

                # extract title and picture.
                title = l_item.css('p').attrib['title']
                href = l_item.css('a').attrib['data-original']

                # try to extract price
                current_price = footer.css('span.price-cp::text')
                if current_price:
                    price = current_price.get()
                else:
                    price = ""

                yield {
                    'Title': title,
                    'Price': price,
                    'Picture href': href
                }

        ###############
        # Scraped the current page entirely. Now we try to scrape the next page.
        ###############
        anchor = response.css('ul.pagination').css('li').css('a.next')
        # contains the url to next page or None.
        next_page = anchor.attrib.get('href', None)

        if next_page:
            # load the next page from url. parse the nextpage.
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse)
