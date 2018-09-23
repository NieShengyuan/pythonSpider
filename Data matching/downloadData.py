'''
下载2011-2017中国医药工业100强排名数据，并将其保存在Excel和文本文档中
Excel读写
文本文档读写
正则匹配
'''
import requests
import re
import xlwt
from string import digits

url_datas = [
    #'http://www.yytj.org.cn/Info.aspx?newsid=227',#2011
    'http://www.yytj.org.cn/Info.aspx?newsid=246',#2012
    'http://www.yytj.org.cn/Info.aspx?newsid=278',#2013
    'http://www.yytj.org.cn/Info.aspx?newsid=335',#2014
    'http://www.yytj.org.cn/Info.aspx?newsid=337',#2015
    'http://www.yytj.org.cn/Info.aspx?newsid=338',#2016
    'http://www.yytj.org.cn/Info.aspx?newsid=341',#2017
]

def getData(url,year):
    '''
    :param url:数据所在连接
    :param dir: 文件保存位置
    :param cow: 文件保存所在列位置
    :return:
    '''
    print("Start parsing data...")
    global NUM
    html = requests.get(url,data=None)
    print(html.text)
    #pattern = re.compile('<td class="xl66" .*? face="楷体">(.*?)</font></td>')#2017
    #pattern = re.compile('<td class="xl67" .*? face="宋体">(.*?)</font></td>')  # 2016
    #pattern = re.compile('<td class="xl67" width="401".*? face="宋体">(.*?)</font></td>')  # 2014
    pattern = re.compile('0pt">(.*?)<span lang="EN-US".*?</p>') #2013
    #pattern = re.compile('<p style="margin-bottom: 7.5pt; line-height: 20.25pt">.*?face="宋体">(.*?)<span lang=')#2012
    #pattern = re.compile('<p><span style="white-space: nowrap">(.*?)</span></p>')#2011
    result = re.findall(pattern,html.text)
    print("---------------------------------------------")
    print(result)
    print("\n---------------finsh------------------------\n")
    #开始保存数据
    saveData(result,year)

def saveData(dat,year):
    num = 0
    print("start save data...")
    for d in dat:
        dd = "".join(d.split())  # 去除字符串1\xa0\xa0广州医药集团有限公司其他符号
        sheet1.write(num, year, dd.translate(str.maketrans('', '', digits)))  # 行列, 第三个是要写入的数据
        num+=1
        print(num)
    f.save(r"E:\2018project\PharmaceuticalIndustryData\data"+str(2013)+".xlsx")
    print("save finsh...")

if __name__ == "__main__":
    URL = r"http://www.yytj.org.cn/Info.aspx?newsid=278"  #
    YEAR = 0
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet(u'2011-2017', cell_overwrite_ok=True)  # 创建sheet
    getData(URL,YEAR)
    #saveData()

    print("-----------finsh project-------")
