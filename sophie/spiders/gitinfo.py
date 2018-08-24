# -*- coding: utf-8 -*-
import scrapy
from sophie.items import SophieItem

class GitinfoSpider(scrapy.Spider):
    name = 'gitinfo'
    #allowed_domains = ['github.com']

    #start_urls = ['http://github.com/']
    @property
    def start_urls(self):
        urls ='https://github.com/shiyanlou?page={}&tab=repositories'
        return (urls.format(i) for i in range(1,5))



    def parse(self, response):
        for url in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            item = SophieItem({
                   "name":url.xpath(".//a/text()").extract_first().strip(),
                   "update_time":url.xpath(".//div[3]/relative-time/@datetime").re_first("(\S+)")
                 })
            yield item



