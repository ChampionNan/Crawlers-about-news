#coding:utf-8
import importlib
import sys
import re
import urllib
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

importlib.reload(sys)

driver = webdriver.Chrome()
driver.get("http://slide.news.sina.com.cn/c/")
soup = BeautifulSoup(driver.page_source,'html.parser')
page = 0
i = 0
while page<2:
    for news in soup.select('#eData'):
        for i in range(16):
            title = news.select('h3')[i].text
            href = news.select('a')[i]['href']
           # time = re.findall(r"2019-\d+-\d+ \d+:\d+:\d+",news.select('dd')[0])
            print(title, href)
    driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
    page = page + 1
    time.sleep(3)
    print(title,href)

driver.quit()

#coding:utf-8
import importlib
import sys
import re
import urllib
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
importlib.reload(sys)

driver = webdriver.Chrome()
driver.get("http://slide.news.sina.com.cn/c/")
page = 0
i = 0
while page<5:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for news in soup.select('#SI_Cont .mod-bd clearfix'):
        for i in range(16):
            title = news.select('.item')[i].text
            href = news.select[i]('.item')[i]['href']
           # time = re.findall(r"2019-\d+-\d+ \d+:\d+:\d+",news.select('dd')[0])
            print(title, href)
        i = 0
    driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
    page = page + 1
    time.sleep(3)

driver.quit()

