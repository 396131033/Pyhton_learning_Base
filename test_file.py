#-*-  coding = utf-8 -*-  
#@Time : 2020/8/10 21:15
#@Author : 贾先圆
#@File: test_file.py
#@Software: PyCharm

"""
f = open('test.txt','w')
f.write('I am here,come on!')
f.close()     #注意，open和close应当成对出现
"""

f = open('test.txt','r')

content = f.read(5)
print(content)

f.close()

