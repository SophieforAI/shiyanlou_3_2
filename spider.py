
import json

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

results = []
def parse(response):
    for comment in response.css('div.comment-list-item'):
        results = []
        result = {}
        result['comments'] = comment.css('div.comment-item-content p::text').extract_first()
        result['username']=comment.css('div.user-username a::text').extract_first().strip()
        results.append(result)

def has_next_page(response):
    next_page = True
    if response.xpath('.//*[@id="comments"]/div/div[4]/ul/li[7]/@class').extract_first()[0] =='disabled':
        next_page = False
    return next_page

def goto_next_page(driver):
    pass

def wait_page_return(driver,page):
    WebDriverWait(driver,10).unyil(
            EC.text_to_be_present_in_element(
               (By.XPATH,'//ul[@class="pagination"]/li[@class="active"]'),
            str(page)
            )
            )
def spider():
    driver = webdriver.PhantomJS()
    url = '//ul[@class="pagination"]/li[@class="active"]'
    driver.get(url)
    page=1
    while True:
        wait_page_return(driver,page)
        html = driver.page_source
        response=HtmlResponse(url=url.body=html.encode('utf8'))
        parse(response)
        if not has_next_page(response):
            break
        page+=1
        goto_next_page(driver)
    with open('/home/shiyanlou/comments.json','w') as f:
        f.write(json.dums(results))

if __name__=='__main__':
    spider()
