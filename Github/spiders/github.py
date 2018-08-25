# -*- coding: utf-8 -*-
import scrapy
from Github.items import GithubItem

class GithubSpider(scrapy.Spider):
    name = 'github'
    #allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?page={}&tab=repositories'.format(i) for i in range(1,5)]

    def parse(self, response):
        for url in response.css('li.col-12'):
            item = GithubItem()
            item['name']=url.xpath(".//a/text()").extract_first().strip()
            item['update_time']=url.xpath(".//div[3]/relative-time/@datetime").re_first("(\S+)")
            inner_url = response.urljoin(url.xpath('.//@href').extract_first())
            request = scrapy.Request(inner_url,callback=self.parse_next)        
            request.meta['item']=item
            yield request

    def parse_next(self,response):
        item = response.meta['item']
        item['commits']=response.css('li.commits span::text').re_first('\d+')
        item['branches']=response.xpath('//li[2]/a/span/text()').re_first('\d+')
        item['releases']=response.xpath('//li[3]/a/span/text()').re_first('\d+')
        yield item


