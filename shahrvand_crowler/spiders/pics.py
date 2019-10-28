# -*- coding: utf-8 -*-
import scrapy
import requests
import shutil


class PicsSpider(scrapy.Spider):
    name = 'pics'

    allowed_domains = ['shahrvand.ir']
    start_urls = [l.strip() for l in open('product_links.txt').readlines()]

    def parse(self, response):
        code =  response.css("div.code").css("span::text").extract_first()
        link = response.css("div.single_slideshow_big").css("img").xpath('@data-large-img-url').get()
        if code is not None:
            img = requests.get(link, stream=True)
            local_file = open( './images/' + str(code) + '.jpg', 'wb')
            img.raw.decode_content = True
            shutil.copyfileobj(img.raw, local_file)
            del img
            print("download image {} complete".format(code))