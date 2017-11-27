# -*- coding: utf-8 -*-
# 获取页面隐藏元素，网盘链接及密码
# 测试页面：http://m.mei123478.com/
# 页面描述：网盘链接和密码隐藏，所以第一步需要注入js进行显示，然后正常进行文本解析，因为字段比较简单，所以直接字符串解析了
# 注意：使用phantomjs等待时间比较久,所以调试是一个比较累人的工作
# 2017.11.20: 修复多值检索项的匹配问题
# 2017.11.27: 重构检索结构

from selenium import webdriver
from selenium.webdriver.support.select import Select
import os,time
import urllib

def getUP(searchKey):
    '''
    Input:searchKey u'生活大爆炸'
    Return: {searchKey:[(introword,link,password),]}
    
    '''
    url_main= 'http://m.mei123478.com/?s='
    pre_url = url_main + urllib.quote_plus(searchKey.encode('utf8'))

    # 第一部分：获取检索项进行重构url
    driver_detail = webdriver.PhantomJS()
    driver_detail.get(pre_url)
    article_list = driver_detail.find_elements_by_xpath("//div[@class='article']/h2/a")
    url_find = 'NoFound'
    for article in article_list:
        if searchKey.encode('utf8') in article.text.encode('utf8'):
            url_find = article.get_attribute('href')
            break

#     print url_find 
    
    if url_find != 'NoFound':
        driver_detail.get(url_find)

        # 第二部分：将隐藏元素显现，设置display='block'
        # thanks for :https://www.cnblogs.com/fnng/p/5365900.html
        # 注入js脚本，开启所有包含网盘内容的h2标签
        js = '''
        var urlpw = document.querySelectorAll("h2");
        var size_ = urlpw.length;
        for (i=0;i<size_;i++){urlpw[i].style.display='block'}
        '''
        driver_detail.execute_script(js)

        # 第三部分，解析隐藏字段，解析出网盘链接和密码
        #url_ = driver_detail.find_elements_by_xpath("//h2[@style='display: block;']")
        url_ = driver_detail.find_elements_by_xpath("//span[@style='color: #ff0000;']")  # 使用颜色属性，缩小范围
        urlpw = []    

        for hide in url_:
            innerHtml = hide.get_attribute("innerHTML")
            #print hide.text  # 度盘点我  密码: siua
            if 'http' in innerHtml:
                url = innerHtml.split("href=\"")[-1].split("\">")[0]
                introword = innerHtml.split("href=\"")[-1].split("\">")[-1].split("<")[0].strip()
                #print url
                if u'密码' in innerHtml:
                    pw = hide.text[-4:]
                    #print pw
                else:
                    #print 'No Password,just watch'
                    pw = 'NoPW'
                urlpw.append((introword,url,pw))

        driver_detail.quit()
        return {searchKey:urlpw}
    else:
        return 'No Found or change the title try again!'

if __name__ == '__main__':
    
    test = [u'美国恐怖故事']#,u'当你沉睡时', u'无耻之徒',u'生活大爆炸']
    for i in test:
        urlpw = getUP(i)
        print urlpw
        print '-----'
#     urlpw = getUP(u'美国恐怖故事')
#     print urlpw


