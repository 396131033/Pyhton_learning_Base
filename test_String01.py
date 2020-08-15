#-*-  coding = utf-8 -*-  
#@Time : 2020/8/10 9:50
#@Author : 贾先圆
#@File: test_String01.py
#@Software: PyCharm

word ='字符串'
sentence = "这是一个句子"

paragraph = """
    这是一个段落
    可以有多个行组成
"""

print(word)
print(sentence)
print(paragraph)

my_str = "I'm a student"
my_str = 'I\'m a student'  #第二个单引号需要输出，所以需要转译  \
my_str = "I'm a student"  #双引号里可以包含单引号，不用转译符号
print(my_str)
