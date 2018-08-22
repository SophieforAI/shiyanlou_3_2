# -*- coding=utf-8 -*-
import scrapy

class ShiyanlouScrapy(scrapy.Spider):
    name ="shiyanlou_spider"
    @property
    def start_urls(self):
        urls = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = 'https://github.com/shiyanlou?page=2&tab=repositories'
        return (urls.format(i) for i in range(0,5))

    def parse(self,response):
        for url in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            yield {
                "name":url.xpath("a/text()").extract(),
                "update_time":url.xpath("/div[3]/@relative-time").extract()
            }

