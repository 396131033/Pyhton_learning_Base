#-*-  coding = utf-8 -*-  
#@Time : 2020/8/10 11:19
#@Author : 贾先圆
#@File: test_list.py
#@Software: PyCharm

import random

offices = [[],[],[]]
names = ['A','B','C','D','E','F','G','H']

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

for i,office in enumerate(offices):
    print('the length of office{} is {}'.format(i,len(offices[i])),end='\n')
    for j in office:
        print(j,end = '\t')
    print('\n')