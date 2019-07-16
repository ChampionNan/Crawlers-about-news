#新浪新闻
#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

url = "https://news.sina.com.cn/china/"
wbdata = requests.get(url)
wbdata.encoding = 'utf-8'
soup = BeautifulSoup(wbdata.text,'html.parser')
i=0

def Nofind(title):
    if(title.find("降低") != -1):
        return -1
    if(title.find("对外") != -1):
        return -1
    if(title.find("整齐") != -1):
        return -1
    if(title.find("对外") != -1):
        return -1

def Select(title):
    if(title.find(str("xx")) != -1 and Nofind(title) != -1):
        return 1

print("\n-----News in the front page.-----\n\n-----1.news in the left-content.-----\n")
for news in soup.select('.left-content'):
    for i in range(7):
        title = news.select('a')[i].text
        href = news.select('a')[i]['href']
        time = re.findall(r"2019\d+",news.select('img')[0]['src'])
        if(Select(title) == 1):
            print(time,title[2:len(title) - 2], ':', href)
i=0
print('\n-----2.news in the right-content-----\n')
for news in soup.select('.right-content'):
    for i in range(10):
        title = news.select('a')[i].text
        href = news.select('a')[i]['href']
        time = re.findall(r"2019-\d+-\d+", href)
        if(Select(title) == 1):
            print(time,title, ':', href)
i=0
print('\n-----3.news in the news-2 -----','\n')
for news in soup.select('.news-2'):
    for i in range(11):
        title = news.select('a')[i].text
        href = news.select('a')[i]['href']
        time = re.findall(r"2019\-\d+-\d+", href)
        if(Select(title) == 1):
            print(time,title, ':', href)
print("\n-----4.news in the switch-text-----\n")
for news in soup.select('.switch-text'):
    for i in range(8):
        title = news.select('a')[i].text
        href = news.select('a')[i]['href']
        time = re.findall(r"2019\d+", news.select('img')[0]['src'])
        if(Select(title) == 1):
            print(time,title[2:len(title) - 2], ':', href)
