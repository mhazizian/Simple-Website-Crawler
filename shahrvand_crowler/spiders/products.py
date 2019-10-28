# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    # allowed_domains = ['http://www.shahrvand.ir']

    # baseurl = 'http://www.shahrvand.ir/fa/product.html#/pagesize-32/page-{page_num}'
    baseurl = 'http://www.shahrvand.ir/fa/product.html&pagesize[]=300&page[]={page_num}&ajax=ok?_=1572060820237'
    first = True

    start_urls = [
        'http://www.shahrvand.ir/fa/product.html&pagesize[]=300&page[]=32&ajax=ok?_=1572060820237'
    ]

    def parse(self, response):
        for product in response.css("div.product"):
            link = product.css("a").xpath('@href').get()
            yield {
                "link" : link
            }

        # if (ProductsSpider.first):
        #     ProductsSpider.first = False
        #     for counter in range(2, 70):
        #         next_page_url = self.baseurl.format(page_num=counter)
        #         yield scrapy.Request(response.urljoin(next_page_url), dont_filter=True)
            
        
