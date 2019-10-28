# -*- coding: utf-8 -*-
import scrapy


class InfoSpider(scrapy.Spider):
    name = 'info'
    allowed_domains = ['shahrvand.ir']
    start_urls = [l.strip() for l in open('product_links.txt').readlines()]
    # start_urls = [
    #     'http://www.shahrvand.ir/fa/product/%D9%84%D9%88%D8%A7%D8%B2%D9%85-%D8%AE%D8%A7%D9%86%DA%AF%DB%8C/%D9%84%D9%88%D8%A7%D8%B2%D9%85-%D8%A8%D8%B1%D9%82%DB%8C-%D8%A2%D8%B4%D9%BE%D8%B2%D8%AE%D8%A7%D9%86%D9%87/%D8%BA%D8%B0%D8%A7-%D8%B3%D8%A7%D8%B2-%D9%87%D8%A7/%DA%AF%D9%88%D8%B4%D8%AA-%DA%A9%D9%88%D8%A8-%D8%A8%D8%B1%D9%82%DB%8C/53555-%DA%AF%D9%88%D8%B4%D8%AA-%DA%A9%D9%88%D8%A8-%D8%A8%D8%B1%D9%82%DB%8C-%D9%85%D8%AF%D9%84-HM105-%D9%85%D8%AA%D8%A6%D9%88.html'
    # ]

    def parse(self, response):
        res = {
            "code" : response.css("div.code").css("span::text").extract_first(),
            "name" : response.css("div.title").css("h1::text").extract_first()
        }
        res['desc'] = {}
        for ul in response.xpath("//div[@class='single_tab2_right']/ul"):
            for li in ul.css('li'):
                key = li.css("span::text").extract_first()
                value = str(li.css("p::text").extract_first()).strip()
                res['desc'][key] = value
                print(key)

        yield res

