import json
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

results =[]
def parse(response):
    for comment in response.css('div.comment-list-item'):
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
    driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()

def wait_page_return(driver,page):
    WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//ul[@class="pagination"]/li[@class="active"]'),
            str(page)
        )
    )

def spider():
    driver = webdriver.PhantomJS()
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    page=1
    while True:
        wait_page_return(driver,page)
        html = driver.page_source
        response=HtmlResponse(url=url,body=html.encode('utf8'))
        parse(response)
        '''
        if not has_next_page(response):
            break
        '''
        if response.css('li.disabled.next-page'):
            break
        page+=1
        print(page)
        goto_next_page(driver)
    with open('/home/shiyanlou/comments.json','w') as f:
        json.dump(results, f)

if __name__=='__main__':
    spider()
