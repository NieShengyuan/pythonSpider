# _*_ coding:utf-8_*_
# auther :nsy12
# date   :2018/2/26
# time   :16:20
# !/usr/bin/env python
# coding=utf-8

import os
import time
import random
import threading
from multiprocessing import Pool, cpu_count

import requests, re
from bs4 import BeautifulSoup

global index

header = {

    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.46es.com',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36'
}


def make_dir(folder_name):
    """ 新建套图文件夹并切换到该目录下
    """
    path = os.path.join(DIR_PATH, folder_name)
    # 如果目录已经存在就不用再次爬取了，去重，提高效率。存在返回 False，否则反之
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
        os.chdir(path)
        return True
    print("Folder has existed!")
    return False


def delete_empty_dir(dir):
    """ 如果程序半路中断的话，可能存在已经新建好文件夹但是仍没有下载的图片的情况
    但此时文件夹已经存在所以会忽略该套图的下载，此时要删除空文件夹
    """
    if os.path.exists(dir):
        if os.path.isdir(dir):
            for d in os.listdir(dir):
                path = os.path.join(dir, d)  # 组装下一级地址
                if os.path.isdir(path):
                    delete_empty_dir(path)  # 递归删除空文件夹
        if not os.listdir(dir):
            os.rmdir(dir)
            print("remove the empty dir: {}".format(dir))
    else:
        print("Please start your performance!")  # 请开始你的表演


lock = threading.Lock()  # 全局资源锁


def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def save_pic(pic_src, pic_cnt):
    """ 将图片下载到本地文件夹
    """
    index = 0
    try:
        picture_html = requests.get(pic_src, data=None, headers=header)
        # 解析出所有图片链接
        picture_url = re.findall('img src="(.*?)" >', picture_html.text)
        time.sleep(random.randint(1, 2))

        for link in picture_url:
            img = requests.get(src, headers=headers)
            time.sleep(random.randint(1, 2))
            with open(str(index) + ".jpg", 'ab') as f:
                f.write(img.content)
                print("img" + str(index) + "success")
                index = index + 1


    except Exception as e:
        print(e)


def main():
    try:

        # with lock:

        for n in range(3, 15):
            ip_url = 'http://www.xicidaili.com/nn/'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            }
            ip_list = get_ip_list(ip_url, headers=headers)
            #proxies = get_random_ip(ip_list)
            proxies = '58.216.202.149'

            urls = "http://www.***.com//html/part/19_" + str(n) + ".html"
            url_home = 'http://www.***.com'
            print("page" + str(n))
            html = requests.request('GET', url_home, data=None, headers=header, proxies=proxies)
            html = requests.request('GET', urls, data=None, headers=header, proxies=proxies)
            print(html.text)
            html.encoding = 'gbk'
            folder_url = re.findall('<a href="(.*?)" title=".*?" target="_blank">', html.text)
            folder_name = re.findall('<a href=".*?" title="(.*?)" target="_blank">', html.text)

            time.sleep(random.randint(1, 2))
            # 每页20个套图
            for num in range(1, 20):
                get_url = "http://www.***.com" + str(folder_url[num])
                make_dir(folder_name[num])
                save_pic(get_url, num)
                print("page" + str(num) + "success")
                time.sleep(random.randint(1, 2))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

