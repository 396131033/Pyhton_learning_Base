#-*-  coding = utf-8 -*-  
#@Time : 2020/8/9 20:22
#@Author : 贾先圆
#@File: test01.py
#@Software: PyCharm

a = 10
print('我今年%d岁'%a)
print("hell world")
print('我的名字是%s,我的国籍是%s'%('贾先圆','中国'))
print('我的名字是\t{},\n我的国籍是：{}'.format('贾先圆','中国'))
print('www','baidu','com',sep='.')
print('hello',end='')
print('world',end='\t')
print('python',end='\n')
print('end')

password = input("请输入密码：")
print(type(password))
print('您刚刚输入的密码是：',password)
