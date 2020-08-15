#-*-  coding = utf-8 -*-  
#@Time : 2020/8/10 20:31
#@Author : 贾先圆
#@File: test_func.py
#@Software: PyCharm

'''
def printinfo():
    print('='*20)
    print('   人生苦短，我用Python!    ')
    print('='*20)

printinfo()


def add2num (a,b):
    return a+b

c = add2num(10,20)
print(c)

def divid (a,b):
    shang =a//b
    yushu = a%b
    return shang,yushu  #同时返回多个值

a,b = divid(5,2)  #需要使用多个值来保存返回值
print(a,b)
'''

'''
def line():
    print('-'*20)

def n_Line(n):
    if 'int' in str(type(n)):  #判断是否为数字
        for i in range(n):
            line()
    else:
        print("您输入有误，请输入一个整数")

n = 'a'
n_Line(n)
'''


'''
def three_Sum(a,b,c):
    return a+b+c

def three_Average(a,b,c):
    tmp = three_Sum(a,b,c)
    return tmp/3

average = three_Average(4,5,6)
print(average)
'''

# 全局变量

a = 100

def test1():
    global a
    print('全局变量',a)
    a = 200
    print('修改全局变量',a)
    print('='*20)

def test2():
    print('test2中的a,代表全局变量',a)
    print('='*20)

def test3():
    # # 未定义局部变量之前
    # print('未定义局部变量之前：',a)
    print('-'*30)
    a = 600  #局部变量
    print('修改前局部变量',a)
    a = 6600
    print('修改后局部变量',a)
    print('='*20)

test2()
test1()
test2()

test3()