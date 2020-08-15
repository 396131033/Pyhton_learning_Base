#-*-  coding = utf-8 -*-  
#@Time : 2020/8/9 22:39
#@Author : 贾先圆
#@File: test03.py
#@Software: PyCharm



# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} * {} = {}'.format(j,i,i*j),end='\t')
#     print('\n')

m = 1
while m<=9:
    n = 1
    while n<m+1:
        print('{} * {} = {}'.format(n, m, m * n), end='\t')
        n += 1
    m += 1
    print('\n')


