#_*_ coding:utf-8_*_
# auther :nsy12
# date   :2018/1/30
# time   :18:32
# movie Project

import requests #下载网页源代码
import re       #正则表达式模块，提取数据
import time
import random


print ("please wait...system loding...")
header = {
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.ygdy8.net',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36'
}

for m in range(1,3):  #爬160页
    print("第" +str(m)+"页")
    time.sleep(random.randint(2, 5))
    PostUrl = "http://www.ygdy8.net/html/gndy/dyzz/list_23_"+str(m)+".html" #url的构造方式
    html = requests.post(PostUrl,data=None,headers = header)
    html.encoding = 'gb2312' #指定网页编码方式（查看网页源代码）
    #提取信息，返回的是列表
    #匹配 以<a href="(.*?)" class="ulink">结尾的信息
    date = re.findall('<a href="(.*?)" class="ulink">',html.text) #(.*?)

    for n in date:
        finalUrl = "http://www.ygdy8.net"+n
        html2 = requests.post(finalUrl,data=None,headers = header)
        html2.encoding = 'gb2312'
        #title = re.findall('<title>(.*?)迅雷下载_阳光电影</title>',html2.text)
        ftp = re.findall('<a href="(.*?)">ftp://',html2.text)
        with open(r'E:\Python\pythonProject\movies\date.txt','a',encoding='gb2312') as f:
            f.write(ftp[0]+'\n')
        #print(title)
        print(ftp)












'''
PostUrl_Newest = "http://www.ygdy8.net/html/gndy/dyzz/index.html"
PostUrl_Foreign = "http://www.ygdy8.net/html/gndy/oumei/index.html"
PostUrl_Domestic = "http://www.ygdy8.net/html/gndy/china/index.html"

driver = webdriver.Chrome()
time.sleep(2)
driver.get("http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html")
'''


#def UrlDeal(PostUrl)
#    drive.get(PostUrl)
#    time.sleep(2)
#    print("data analysis...")



#if __name__ == "__main__":
