#-*-  coding = utf-8 -*-  
#@Time : 2020/8/10 22:13
#@Author : 贾先圆
#@File: test_file_train.py
#@Software: PyCharm

def read_File(filename):
    f = open(filename,'r',encoding='gbk')
    data = f.readlines()
    f.close()
    return data

def write_File(filename,data):
    f = open(filename, 'w',encoding='gbk')
    if 'list' in str(type(data)):

        for i in range(len(data)):
            f.write(data[i])
    else:
        f.write(data)
    f.close()

str_shi = """
        宣室求贤访逐臣，贾生才调更无伦。
        可怜夜半虚前席，不问苍生问鬼神。
"""
file1 = "gushi.txt"
file2 = "copy.txt"

try:
    write_File(file1,str_shi)
    data = read_File(file1)
    print('=====正在复制=====')
    write_File(file2,data)
    print('=====复制完毕=====')

except Exception as result:
    print('程序出错，错误信息如下：')
    print(result)

