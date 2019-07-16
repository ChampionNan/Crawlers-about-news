# coding:utf-8
import importlib
from selenium.common.exceptions import NoSuchElementException
import time
from graph import *
from selenium import webdriver

importlib.reload(sys)

def Apart(title):
    #找到某些有好方向的关键字
    if (title.find(str("xx")) != -1 or title.find(str("xx")) != -1):
        return 1

def Select(title):
    if ((title.find(str("xx")) != -1 or title.find(str("xx")) != -1) and Apart(title) != 1):
        return 1

    else:
        return 0


def grab_news():
    driver = webdriver.Chrome()
    driver.get("http://slide.news.sina.com.cn/c/")
    file = open('data.txt', 'w+')
    file.write("-----从新浪网筛选出来的新闻-----\n")
    file.write("序号-----时间-------新闻内容\n")
    #page = int(input("请输入页数 "))
    id = 1
    page = 100
    try:
        while page >= 0:
            items = driver.find_elements_by_class_name('bd')
            count = len(items)
            for i in range(count):
                # print(16 * page + i + 1, ':', items[i].text, '\n')
                title = items[i].text
                if (Select(title) == 1):
                    newstime = re.findall(r"(?:\d+年\d+月\d+日|\d月\d日|\d+年\d+月\d+时)", title)
                    adjusttime = ','.join(newstime)
                    # file.write(id'.'+adjusttime+':'+title)
                    file.write("%d. %s: %s\n" % (id, adjusttime, title))
                    print(id, ':', title)
                    id = id + 1
            driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
            page = page - 1
            time.sleep(1.5)
    except NoSuchElementException as e:
        print(e)

    driver.quit()
    file.write("-----新闻筛选结束，共筛选了%d页共%d条新闻-----" % (page,page*16))
    file.close()


if __name__ == "__main__":
    grab_news()

