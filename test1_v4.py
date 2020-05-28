# -*- codeing = utf-8 -*-
# @Time : 2020/4/27 9:19
# @Author : liuyi
# @File : test1_v4.py
# @Software : PyCharm

# 改r矩阵，现在state表示边，r矩阵反应边的连接关系
# 优先选择非桥：桥0.5
# 转弯：0.8
# 走直线：1
#state 去了 next_state，把state清空，还有能去的除了next state也清空

import numpy as np
import random
np.set_printoptions(threshold = 1e6)

'''
def initiaR():
    r = np.ones((44, 44), dtype=np.float32)
    r = r * (-1)
    r[0, 1] = 1
    r[0, 4] = 1
    r[1, 0] = 1
    r[1, 5] = 1
    r[2, 3] = 1
    r[2, 6] = 1
    r[3, 2] = 1
    r[3, 7] = 1
    r[4, 0] = 1
    r[4, 11] = 1

    r[5, 1] = 1
    r[5, 8] = 0.8
    r[5, 9] = 0.5
    r[5, 13] = 1

    r[6, 2] = 1
    r[6, 9] = 0.1
    r[6, 10] = 0.1
    r[6, 14] = 0.1

    r[7, 3] = 1
    r[7, 16] = 1

    r[8, 5] = 0.8
    r[8, 9] = 0.5
    r[8, 12] = 0.1
    r[8, 13] = 0.8

    r[9, 5] = 0.1
    r[9, 6] = 0.5
    r[9, 8] = 0.1
    r[9, 10] = 1
    r[9, 13] = 0.1
    r[9, 14] = 0.5

    r[10, 6] = 0.1
    r[10, 9] = 0.1
    r[10, 14] = 0.1
    r[10, 15] = 1

    r[11, 4] = 1
    r[11, 17] = 1

    r[12, 8] = 1
    r[12, 17] = 0.1
    r[12, 18] = 0.1
    r[12, 21] = 0.1

    r[13, 5] = 1
    r[13, 8] = 0.8
    r[13, 9] = 0.5
    r[13, 18] = 1

    r[14, 6] = 0.1
    r[14, 9] = 0.1
    r[14, 10] = 0.1
    r[14, 19] = 1

    r[15, 10] = 0.1
    r[15, 19] = 0.8
    r[15, 20] = 0.8
    r[15, 22] = 0.5

    r[16, 7] = 1
    r[16, 20] = 1

    r[17, 11] = 1
    r[17, 12] = 0.1
    r[17, 18] = 0.1
    r[17, 21] = 0.1

    r[18, 12] = 0.1
    r[18, 13] = 1
    r[18, 17] = 0.1
    r[18, 21] = 0.1

    r[19, 14] = 1
    r[19, 15] = 0.8
    r[19, 20] = 1
    r[19, 22] = 0.5

    r[20, 15] = 0.8
    r[20, 16] = 1
    r[20, 19] = 1
    r[20, 22] = 0.5

    r[21, 12] = 1
    r[21, 17] = 0.5
    r[21, 18] = 0.5
    r[21, 23] = 0.1
    r[21, 24] = 0.1
    r[21, 28] = 0.1

    r[22, 15] = 0.1
    r[22, 19] = 0.1
    r[22, 20] = 0.1
    r[22, 25] = 0.5
    r[22, 26] = 0.5
    r[22, 31] = 1

    r[23, 21] = 0.5
    r[23, 24] = 1
    r[23, 27] = 1
    r[23, 28] = 0.8

    r[24, 21] = 0.5
    r[24, 23] = 1
    r[24, 28] = 0.8
    r[24, 29] = 1

    r[25, 22] = 0.1
    r[25, 26] = 0.1
    r[25, 30] = 1
    r[25, 31] = 0.1

    r[26, 22] = 0.1
    r[26, 25] = 0.1
    r[26, 31] = 0.1
    r[26, 32] = 1

    r[27, 23] = 1
    r[27, 36] = 1

    r[28, 21] = 0.5
    r[28, 23] = 0.8
    r[28, 24] = 0.8
    r[28, 33] = 0.1

    r[29, 24] = 1
    r[29, 33] = 0.1
    r[29, 34] = 0.1
    r[29, 37] = 0.1

    r[30, 25] = 1
    r[30, 34] = 0.5
    r[30, 35] = 0.8
    r[30, 38] = 1

    r[31, 22] = 0.1
    r[31, 25] = 0.1
    r[31, 26] = 0.1
    r[31, 35] = 1

    r[32, 26] = 1
    r[32, 39] = 1

    r[33, 28] = 1
    r[33, 29] = 0.1
    r[33, 34] = 0.1
    r[33, 37] = 0.1

    r[34, 29] = 0.5
    r[34, 33] = 1
    r[34, 37] = 0.5
    r[34, 30] = 0.1
    r[34, 35] = 0.1
    r[34, 38] = 0.1

    r[35, 30] = 0.8
    r[35, 31] = 0.1
    r[35, 34] = 0.5
    r[35, 38] = 0.8

    r[36, 27] = 1
    r[36, 40] = 1

    r[37, 29] = 0.1
    r[37, 33] = 0.1
    r[37, 34] = 0.1
    r[37, 41] = 1

    r[38, 30] = 1
    r[38, 34] = 0.5
    r[38, 35] = 0.8
    r[38, 42] = 1

    r[39, 32] = 1
    r[39, 43] = 1
    r[40, 36] = 1
    r[40, 41] = 1
    r[41, 40] = 1
    r[41, 37] = 1
    r[42, 38] = 1
    r[42, 43] = 1
    r[43, 39] = 1
    r[43, 42] = 1


    # for i in range(44):
    #     for j in range(44):
    #         if (i==2 or i==3 or i==6 or i==7 or i==10 or i==14 or i==15 or i==16 or i==19 or i==20) and r[i,j] != -1:
    #             r[i,j] += 3
    #         if (i==25 or i==26 or i==30 or i==31 or i==32 or i==35 or i==38 or i==39 or i==42 or i==43) and r[i,j] != -1:
    #             r[i,j] += 2
    #         if (i==23 or i==24 or i==27 or i==28 or i==29 or i==33 or i==36 or i==37 or i==40 or i==41) and r[i,j] != -1:
    #             r[i,j] += 1


    return r
'''


#拐弯全是0.8
#去桥全是0.5
#走直线（除了桥）全是1
def initiaR():
    r = np.ones((44, 44), dtype=np.float32)
    r = r * (-1)
    r[0, 1] = 1
    r[0, 4] = 1
    r[1, 0] = 1
    r[1, 5] = 1
    r[2, 3] = 1
    r[2, 6] = 1
    r[3, 2] = 1
    r[3, 7] = 1
    r[4, 0] = 1
    r[4, 11] = 1

    r[5, 1] = 0.8
    r[5, 8] = 0.8
    r[5, 9] = 0.5
    r[5, 13] = 1

    r[6, 2] = 0.8
    r[6, 9] = 0.5
    r[6, 10] = 0.8
    r[6, 14] = 1

    r[7, 3] = 1
    r[7, 16] = 1

    r[8, 5] = 0.8
    r[8, 9] = 0.5
    r[8, 12] = 0.8
    r[8, 13] = 0.8

    r[9, 5] = 0.8
    r[9, 6] = 0.8
    r[9, 8] = 1
    r[9, 10] = 1
    r[9, 13] = 0.8
    r[9, 14] = 0.8

    r[10, 6] = 0.8
    r[10, 9] = 0.5
    r[10, 14] = 0.8
    r[10, 15] = 0.8

    r[11, 4] = 1
    r[11, 17] = 1

    r[12, 8] = 0.8
    r[12, 17] = 0.8
    r[12, 18] = 0.8
    r[12, 21] = 0.5

    r[13, 5] = 1
    r[13, 8] = 0.8
    r[13, 9] = 0.5
    r[13, 18] = 0.8

    r[14, 6] = 1
    r[14, 9] = 0.5
    r[14, 10] = 0.8
    r[14, 19] = 0.8

    r[15, 10] = 0.8
    r[15, 19] = 0.8
    r[15, 20] = 0.8
    r[15, 22] = 0.5

    r[16, 7] = 1
    r[16, 20] = 1

    r[17, 11] = 0.8
    r[17, 12] = 0.8
    r[17, 18] = 1
    r[17, 21] = 0.5

    r[18, 12] = 0.8
    r[18, 13] = 0.8
    r[18, 17] = 1
    r[18, 21] = 0.5

    r[19, 14] = 0.8
    r[19, 15] = 0.8
    r[19, 20] = 1
    r[19, 22] = 0.5

    r[20, 15] = 0.8
    r[20, 16] = 0.8
    r[20, 19] = 1
    r[20, 22] = 0.5

    r[21, 12] = 1
    r[21, 17] = 0.8
    r[21, 18] = 0.8
    r[21, 23] = 0.8
    r[21, 24] = 0.8
    r[21, 28] = 1

    r[22, 15] = 1
    r[22, 19] = 0.8
    r[22, 20] = 0.8
    r[22, 25] = 0.8
    r[22, 26] = 0.8
    r[22, 31] = 1

    r[23, 21] = 0.5
    r[23, 24] = 1
    r[23, 27] = 0.8
    r[23, 28] = 0.8

    r[24, 21] = 0.5
    r[24, 23] = 1
    r[24, 28] = 0.8
    r[24, 29] = 0.8

    r[25, 22] = 0.5
    r[25, 26] = 1
    r[25, 30] = 0.8
    r[25, 31] = 0.8

    r[26, 22] = 0.5
    r[26, 25] = 1
    r[26, 31] = 0.8
    r[26, 32] = 0.8

    r[27, 23] = 1
    r[27, 36] = 1

    r[28, 21] = 0.5
    r[28, 23] = 0.8
    r[28, 24] = 0.8
    r[28, 33] = 0.8

    r[29, 24] = 0.8
    r[29, 33] = 0.8
    r[29, 34] = 0.5
    r[29, 37] = 1

    r[30, 25] = 0.8
    r[30, 34] = 0.5
    r[30, 35] = 0.8
    r[30, 38] = 1

    r[31, 22] = 0.5
    r[31, 25] = 0.8
    r[31, 26] = 0.8
    r[31, 35] = 0.8

    r[32, 26] = 1
    r[32, 39] = 1

    r[33, 28] = 0.8
    r[33, 29] = 0.8
    r[33, 34] = 0.5
    r[33, 37] = 0.8

    r[34, 29] = 0.8
    r[34, 33] = 1
    r[34, 37] = 0.8
    r[34, 30] = 0.8
    r[34, 35] = 1
    r[34, 38] = 0.8

    r[35, 30] = 0.8
    r[35, 31] = 0.8
    r[35, 34] = 0.5
    r[35, 38] = 0.8

    r[36, 27] = 1
    r[36, 40] = 1

    r[37, 29] = 1
    r[37, 33] = 0.8
    r[37, 34] = 0.5
    r[37, 41] = 0.8

    r[38, 30] = 1
    r[38, 34] = 0.5
    r[38, 35] = 0.8
    r[38, 42] = 0.8

    r[39, 32] = 1
    r[39, 43] = 1
    r[40, 36] = 1
    r[40, 41] = 1
    r[41, 40] = 1
    r[41, 37] = 1
    r[42, 38] = 1
    r[42, 43] = 1
    r[43, 39] = 1
    r[43, 42] = 1

    return r

r = initiaR()

print(r)

q = np.zeros([44,44],dtype=np.float32)

gamma = 0.8

for step in range(1000):
    state = random.randint(0,43)
    for j in range(44):
        next_state_list=[]
        for i in range(44):
            if r[state,i] != -1:
                next_state_list.append(i)
        next_state = next_state_list[random.randint(0,len(next_state_list)-1)]
        qval = r[state,next_state] + gamma * max(q[next_state]) #注意qval是一个数值
        q[state,next_state] = qval
        state = next_state


print(q)

# .....................................验证...........................................

def findIndex(value, list):
    for i in range(len(list)):
        if value == list[i]:
            return i
    return False


def findPath(start, q):

    linenum = q.shape[0]
    state = start
    print("robot start at {}".format(state))
    while q.any():

        if not q[state].any():  # 如果此state全是0,就遍历找一个不全是0的state,肯定能找到
            for new_state in range(linenum):
                if not q[new_state].any():
                    continue
                print("from {} jump to {}".format(state, new_state))
                state = new_state
                break

        q_max = q[state].max()  # 状态state这一行里的最大值，即回报最大的动作的回报值
        q_max_action = []

        for action in range(linenum):  # 找回报最大的动作的下标
            if q[state, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        print("the robot goes to " + str(next_state) + '.')
        #q[state, next_state] = 0
        #q[next_state, state] = 0

        #。。。。。。。。。。。。。。。。去掉回头路
        for next in range(44):
            if q[state,next] != 0:
                q[next_state,next] = 0
        q[state] = 0  # 和点不一样的地方，边只能经过一次
        q[:,state] = 0
        state = next_state


firststate = [9,21,22,34]  # 从桥开始
for state in firststate:
    print("it's {}st test.........".format(findIndex(state, firststate)+1))
    q1 = q.copy()
    findPath(state, q1)
