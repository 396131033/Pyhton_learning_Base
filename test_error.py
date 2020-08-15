#-*-  coding = utf-8 -*-  
#@Time : 2020/8/10 21:33
#@Author : 贾先圆
#@File: test_error.py
#@Software: PyCharm

# 发生异常，会报错
'''
print('---------test----1---')

f = open('123.txt','r')  #文件不存在 报错

print('---------test----2---')
'''

'''
# 异常捕获   不会报错
try:
    print('---------test----1---')

    f = open('123.txt','r')  #文件不存在

    print('---------test----2---')
except IOError:  #文件没有找到，就是IO(输入输出)错误
    pass
    
'''
'''
try:
    print(num)
# except IOError:    #num 变量名没有定义，所以不属于IO 错误，所以这里没有用
except NameError:
    print("产生错误了。")
    
'''
'''
try:
    print('---------test----1---')

    # 错误1 NameError
    f = open('123.txt', 'r')  # 文件不存在

    print('---------test----2---')
    f.close()

    # 错误2 NameError
    print(num)
except(IOError,NameError):
    print("产生了很大错误。")

try:
    print('---------test----1---')

    # 错误1 NameError
    f = open('test.txt', 'r')  # 文件不存在

    print('---------test----2---')
    f.close()

    # 错误2 NameError
    print(num)
except(IOError,NameError):  #将可能产生的所有异常类型的错误，都放到下面的小括号中
    print("产生了很大错误。")
'''

# 打印错误信息
'''
try:
    print('---------test----1---')

    # 错误1 NameError
    f = open('test.txt', 'r')  # 文件不存在

    print('---------test----2---')
    f.close()

    # 错误2 NameError
    print(num)
except(IOError,NameError) as result:  #将可能产生的所有异常类型的错误，都放到下面的小括号中
    print("产生了很大错误。")

    print('打印错误信息：\n',result)
'''

'''
# 打印所有异常
try:
    print('---------test----1---')

    # 错误1 NameError
    f = open('123.txt', 'r')  # 文件不存在

    print('---------test----2---')
    f.close()

    # 错误2 NameError
    print(num)
except Exception as result:  #会显示错误个数，但是只显示第一个错误信息
    print("产生了很大错误。")

    print('打印错误信息：\n',result)
'''

import time

try:
    # f = open('123.txt','r')  #123.txt 不存在，所以直接出现错误，跳出第一个try
    f = open('test.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)   #中断2秒
            print(content)

    finally:
        f.close()
        print('文件关闭')
except Exception as result:
    print("出现错误,错误信息如下")
    print(result)