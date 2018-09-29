import os

if __name__ == "__main__":
    DIR_PATH = r'E:\JavaProject\尚学堂高淇java300集第二季'
    filesName = os.listdir(DIR_PATH)
    name = filesName[0]
    for num in range(23,109):
        path = r"E:\JavaProject\尚学堂高淇java300集第二季\\" + filesName[num]
        name = filesName[num]
        newName = r"E:\JavaProject\尚学堂高淇java300集第二季\\"+name[0:4] + name[26:]
        print(filesName[num]  +"----------" +newName)
        os.rename(path,newName)#
