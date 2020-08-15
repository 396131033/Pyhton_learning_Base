#-*-  coding = utf-8 -*-  
#@Time : 2020/8/9 21:29
#@Author : 贾先圆
#@File: test02.py
#@Software: PyCharm
import random
while True:
    user_Number = int(input('剪刀（0），石头（1），布（2）：'))
    pc_Number = random.randint(0,2)

    abs_Num = user_Number-pc_Number
    print('差值',abs_Num)

    if user_Number>2 or user_Number<0:
    # if user_Number<0:
    #     print('您的输入有误，请重新输入一个0-2的整数！')
    # elif user_Number>2:
        print('您的输入有误，请重新输入一个0-2的整数！')
    else:
        if abs_Num == 0:
            print('平局，请重新输入！')
            # user_Number = int(input('剪刀（0），石头（1），布（2）：'))
            # pc_Number = random.randint(0, 2)
        elif abs_Num==1:
            print('随机生成的数字为:',pc_Number)
            print('恭喜，你赢了！')
        elif abs_Num==-2:
            print('随机生成的数字为:', pc_Number)
            print('恭喜，你赢了！')
        # elif abs_Num==-1 | abs_Num==2:
        else:
            print('随机生成的数字为:', pc_Number)
            print('哈哈，你输了！')
    # else:
    #     print('您的输入有误，请重新输入一个0-2的整数！')

