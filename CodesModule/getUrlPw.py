# -*- coding: utf-8 -*-
# 获取页面隐藏元素，网盘链接及密码

from selenium import webdriver
from selenium.webdriver.support.select import Select
import os,time
import urllib

def getUP(searchKey):
    #searchKey = u'当你沉睡时'
    url_main= 'http://m.mei123478.com/?s='
    pre_url = url_main + urllib.quote_plus(searchKey.encode('utf8'))

    # 第一部分：获取检索项进行重构url
    driver_detail = webdriver.PhantomJS()
    driver_detail.get(pre_url)
    url = driver_detail.find_element_by_xpath("//div[@class='article']/h2/a").get_attribute('href')
    #print url
    driver_detail.get(url)

    # 第二部分：将隐藏元素显现，设置display='block'
    # thanks for :https://www.cnblogs.com/fnng/p/5365900.html
    js = 'document.querySelectorAll("h2")[0].style.display="block";'
    driver_detail.execute_script(js)
    url_ = driver_detail.find_element_by_xpath("//div[@class='indent']/h2/span/a")
    url = url_.get_attribute('href')

	# 第三部分：获取innerHTML元素，单使用.text的方法不能获取内容
	# 至于为什么不使用innerText: http://blog.csdn.net/magi1201/article/details/44131361
    password_ = driver_detail.find_element_by_xpath("//div[@class='indent']/h2")
    # thanks for：http://www.linuxhub.org/?p=3801
    password =  password_.get_attribute("innerHTML").split("<")[-2][-4:]

	# 若使用innerText
    # password2_ = password_.get_attribute("innerText")
    # password2 = password2_.split(" ")[-1].strip()

    driver_detail.quit()
    return url, password

if __name__ == '__main__':
    url, password = getUP(u'今生是第一次')
    print url, password

