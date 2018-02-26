# _*_ coding:utf-8_*_
# auther :nsy12
# date   :2018/2/25 
# time   :11:20

import requests
import re, os
from bs4 import BeautifulSoup
import time
import random

FILE_DIR = r'E:\1smart Car\paper'
url_datas = [
    'https://smartcar.cdstm.cn:8083/tpftl/8/ce2dcb2e4d53439596469ef40f88d73d.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/b6e8f8918d9345cb95746b105f23808a.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/73f5d464d22b4834a6ffafec20acda02.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/51b564b50d114a459de984c5754163ed.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/415f6ebd72ab4ad3a96528272cd0066f.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/4bc2bc1ff9eb484491a99829a0833d14.html?https://smartcar.cdstm.cn',
    'https://smartcar.cdstm.cn:8083/tpftl/8/bb30be1030e14e0db910977a331b0eae.html?https://smartcar.cdstm.cn'
]

#显示下载的文档名称
def showPdf(pdf_name):
    print(pdf_name + '...')

#保存文档
def savePdf(url, pdf_name):
    response = requests.get(url, data=None, stream=True)
    if not os.path.exists(FILE_DIR):
        os.makedirs(FILE_DIR)
    with open(os.path.join(FILE_DIR, pdf_name), "wb") as pdf_file:
        for content in response.iter_content():
            pdf_file.write(content)


def downOne(url, pdf_name):
    # showPdf(url, pdf_name)
    savePdf(url, pdf_name)
    print(pdf_name + "has been downloaded!!")


def get_urls(url):
    print("Please wait for second ...")
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
        print('------开始保存：', name)
        downOne(url_pdf, str(name))
        # time.sleep(random.randint(1, 2))

        """
        #将数据写入记事本
        # with open(r'D:jishubaogao\date.txt', 'a', encoding='gbk') as f:
            f.write(name + '\n')
        """


if __name__ == "__main__":

    for url_data in url_datas:
        get_urls(url_data)
        print("finsh"+url_data)

    print("finsh download")
