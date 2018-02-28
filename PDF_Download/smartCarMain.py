# _*_ coding:utf-8_*_
# auther :nsy12
# date   :2018/2/25 
# time   :11:20

import requests
import re, os
from bs4 import BeautifulSoup
import time
import random

global NUM

url_datas = [
    'https://smartcar.cdstm.cn:8083/tpftl/8/ce2dcb2e4d53439596469ef40f88d73d.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/b6e8f8918d9345cb95746b105f23808a.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/73f5d464d22b4834a6ffafec20acda02.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/51b564b50d114a459de984c5754163ed.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/415f6ebd72ab4ad3a96528272cd0066f.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/4bc2bc1ff9eb484491a99829a0833d14.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/bb30be1030e14e0db910977a331b0eae.html?https://smartcar.cdstm.cn'
]


def download(url, pdf_name, dir):
    '''
    判断文件是否存在，若不存在则下载，需要在程序启动前获取文件列表
    :param url: 指向文档的URL
    :param pdf_name: 文档名称
    :param dir: 保存地址
    :return:
    '''
    # showPdf(url, pdf_name)
    # 判断文件是否存在
    if pdf_name in files:
        print(pdf_name + '  exist')
    else:
        response = requests.get(url, data=None, stream=True)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(os.path.join(dir, pdf_name), "wb") as pdf_file:
            for content in response.iter_content():
                pdf_file.write(content)
        print("    " + pdf_name + " has been downloaded!!")


def get_urls(url, dir):
    '''
    对URL指向的网站进行解析，获取文档链接
    :param url: 需解析的URL
    :param dir: 文档保存路径
    :return:
    '''
    print("Please wait for second ...")
    global NUM
    html = requests.get(url, data=None)
    # html.encoding = 'utf-8'  # 指定网页编码方式（查看网页源代码）
    # print(html.encoding)
    # print(html.status_code)
    # print(html.text)

    soup = BeautifulSoup(html.text, 'lxml')
    # all_a = soup.find('div', class_='cvideotitle').find_all('a')
    all_a = soup.find('div').find_all('a')
    for a in all_a:
        title = a.get_text()
        url_pdf = a['href']
        name = title[19:-18]

        print(str(NUM) + '       开始保存：' + name)
        NUM = NUM + 1
        download(url_pdf, str(name), dir)
        # time.sleep(random.randint(1, 2))

        """
        #将数据写入记事本
        # with open(r'D:jishubaogao\date.txt', 'a', encoding='gbk') as f:
            f.write(name + '\n')
        """


if __name__ == "__main__":
    global NUM
    FILE_DIR = r'E:\\1smart Car\paper\Twelfth'
    files = os.listdir(FILE_DIR)  # 读取文件夹下存在的文件

    NUM = 1
    for url_data in url_datas:
        get_urls(url_data, FILE_DIR)
        print("finsh" + url_data)

    print("             finsh download")
