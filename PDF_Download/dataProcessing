# _*_ coding:utf-8_*_
# auther :nsy12
# date   :2018/2/28 
# time   :16:25
# 筛选关键字，并将文件分类保存
import os
import shutil

global NUM, RESULT


def name_analyze(sub, dir):
    '''
    :param sub: 待筛选字符串
    :param dir: 待保存地址
    :return:
    '''
    global RESULT
    # 筛选关键词
    result1 = sub.find('双车')
    result2 = sub.find('追逐')

    if result1 == -1:
        result1 = 0
    if result2 == -1:
        result2 = 0
    # 筛选条件
    if (result1 or result2) != 0:
        # 操作函数
        fileClassify(sub, dir)
        RESULT += 1
        print('   exist' + str(sub))


def fileClassify(fileName, dir):
    '''
    :param fileName:待移动文件名
    :param dir: 待移动新地址
    :return:
    '''
    # 创建文件夹
    if not os.path.exists(dir):
        os.makedirs(dir)
    filesDirs = os.listdir(dir)
    # 查重
    if fileName in filesDirs:
        print(fileName + '  exist')
    else:
        shutil.copy(DIR_PATH + '/' + str(fileName), dir)  # ("oldpos", "newpos")  # 移动文件或目录
        print("    " + fileName + " has been moved!!")


if __name__ == "__main__":
    global NUM, RESULT
    NUM = 1
    RESULT = 1
    # 待筛选地址
    DIR_PATH = 'E:\\1smart Car\paper\Twelfth'
    # 待保存地址
    NEW_DIR = 'E:\\1smart Car\paper\sc'
    files = os.listdir(DIR_PATH)

    for file in files:
        name_analyze(file, NEW_DIR)
        NUM += 1
        print(NUM)

    print("共计" + str(RESULT) + "个结果")
