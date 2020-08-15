#-*-  coding = utf-8 -*-  
#@Time : 2020/8/10 15:38
#@Author : 贾先圆
#@File: test_tuple01.py
#@Software: PyCharm
"""

tup1 = ()
print(type(tup1))

tup2 = (50)
print(type(tup2))

tup3 = (50,)
print(type(tup3))

tup4 = (50,60,70)
print(type(tup4))

"""
# tup1 = ('abc','ddkkl',123,456)
# print(tup1[0])
# print(tup1[-1])
# print(tup1[1:4])


# dictionary
info = {'name':'吴彦祖','age':18,'id':1}
# print(info.keys())
# print(info.values())
# print(info.items())

for key in info.keys():
    print(key)
print('='*20)

for values in info.values():
    print(values)

print('='*20)
for key,value in info.items():
    print('key = {},value = {}'.format(key,value))

a = dict([('a',1),('b',2)])
print(a)


