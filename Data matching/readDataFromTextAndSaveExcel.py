'''
读取文本文档中的数据序列，与基准文本数据序列匹配，并将位置写入Excel文件
'''
import xlrd
from xlutils.copy import copy
def addData(row,col,data):
    '''
    对指定位置插入指定数据
    :param row: 行
    :param col: 列
    :param data: 排名数据
    :return:
    '''
    #写入数据
    sheet = wb.get_sheet(0)
    sheet.write(row,col,data)

def dealData(dir,num):
    '''
    打开一个记事本，对其中数据进行处理
    :param dir: 文档位置
    :param num: 插入列位置
    :return:
    '''
    global lastPos_Company
    #打开当前数据
    data = []
    for line in open(dir,"r"):
        data.append(line[:-1])
    print(data)
    #开始数据处理
    for i in range(0,100):
        nameA = DATA[i]
        for j in range(0,100):
            result = nameA.find(data[j])
            if result == 0:  #找到
                addData(i,num,int(j+1))
                print(str(i)+DATA[i]+'----'+data[j]+str(j+1))

if __name__== "__main__":
    DATA = []
    lastPos_Company = 100
    #文档地址
    file = r"E:\2018project\PharmaceuticalIndustryData\dataFinal.xlsx"
    DIR = r"E:\2018project\PharmaceuticalIndustryData\data2017.txt"
    dir = r"E:\2018project\PharmaceuticalIndustryData\data2011.txt"
    # 打开文件
    rb = xlrd.open_workbook(file, formatting_info=False)
    # 获取sheet
    r_sheet = rb.sheet_by_index(0)
    wb = copy(rb)
    #读取基准文档数据
    print("start read document...")
    for line in open(DIR,"r"):
        DATA.append(line[:-1])
    print(DATA)
    #开始数据处理
    print("start ansys data...")
    dealData(dir,7)
    # 保存数据
    wb.save(file)

