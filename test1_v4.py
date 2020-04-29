# -*- codeing = utf-8 -*-
# @Time : 2020/4/27 9:19
# @Author : liuyi
# @File : test1_v4.py
# @Software : PyCharm

# 改r矩阵，现在state表示边，r矩阵反应边的连接关系
import numpy as np
import random
np.set_printoptions(threshold = 1e6)


def initiaR():
    r = np.ones((44, 44), dtype=np.int16)
    r = r * (-1)
    r[0, 1] = 0
    r[0, 4] = 0
    r[1, 0] = 0
    r[1, 5] = 0
    r[2, 3] = 0
    r[2, 6] = 0
    r[3, 2] = 0
    r[3, 7] = 0
    r[4, 0] = 0
    r[4, 11] = 0
    r[5, 1] = 0
    r[5, 8] = 0
    r[5, 9] = 0
    r[5, 13] = 0
    r[6, 2] = 0
    r[6, 9] = 0
    r[6, 10] = 0
    r[6, 14] = 0
    r[7, 3] = 0
    r[7, 16] = 0
    r[8, 5] = 0
    r[8, 9] = 0
    r[8, 12] = 0
    r[8, 13] = 0

    r[9, 5] = 0
    r[9, 6] = 0
    r[9, 8] = 0
    r[9, 10] = 0
    r[9, 13] = 0
    r[9, 14] = 0

    r[10, 6] = 0
    r[10, 9] = 0
    r[10, 14] = 0
    r[10, 15] = 0
    r[11, 4] = 0
    r[11, 17] = 0
    r[12, 8] = 0
    r[12, 17] = 0
    r[12, 18] = 0
    r[12, 21] = 0
    r[13, 5] = 0
    r[13, 8] = 0
    r[13, 9] = 0
    r[13, 18] = 0
    r[14, 6] = 0
    r[14, 9] = 0
    r[14, 10] = 0
    r[14, 19] = 0
    r[15, 10] = 0
    r[15, 19] = 0
    r[15, 20] = 0
    r[15, 22] = 0
    r[16, 7] = 0
    r[16, 20] = 0
    r[17, 11] = 0
    r[17, 12] = 0
    r[17, 18] = 0
    r[17, 21] = 0
    r[18, 12] = 0
    r[18, 13] = 0
    r[18, 17] = 0
    r[18, 21] = 0
    r[19, 14] = 0
    r[19, 15] = 0
    r[19, 20] = 0
    r[19, 22] = 0
    r[20, 15] = 0
    r[20, 16] = 0
    r[20, 19] = 0
    r[20, 22] = 0

    r[21, 12] = 0
    r[21, 17] = 0
    r[21, 18] = 0
    r[21, 23] = 0
    r[21, 24] = 0
    r[21, 28] = 0

    r[22, 15] = 0
    r[22, 19] = 0
    r[22, 20] = 0
    r[22, 25] = 0
    r[22, 26] = 0
    r[22, 31] = 0

    r[23, 21] = 0
    r[23, 24] = 0
    r[23, 27] = 0
    r[23, 28] = 0
    r[24, 21] = 0
    r[24, 23] = 0
    r[24, 28] = 0
    r[24, 29] = 0
    r[25, 22] = 0
    r[25, 26] = 0
    r[25, 30] = 0
    r[25, 31] = 0
    r[26, 22] = 0
    r[26, 25] = 0
    r[26, 31] = 0
    r[26, 32] = 0
    r[27, 23] = 0
    r[27, 36] = 0
    r[28, 21] = 0
    r[28, 23] = 0
    r[28, 24] = 0
    r[28, 33] = 0
    r[29, 24] = 0
    r[29, 33] = 0
    r[29, 34] = 0
    r[29, 37] = 0
    r[30, 25] = 0
    r[30, 34] = 0
    r[30, 35] = 0
    r[30, 38] = 0
    r[31, 22] = 0
    r[31, 25] = 0
    r[31, 26] = 0
    r[31, 35] = 0
    r[32, 26] = 0
    r[32, 39] = 0
    r[33, 28] = 0
    r[33, 29] = 0
    r[33, 34] = 0
    r[33, 37] = 0

    r[34, 29] = 0
    r[34, 30] = 0
    r[34, 37] = 0
    r[34, 30] = 0
    r[34, 35] = 0
    r[34, 38] = 0

    r[35, 30] = 0
    r[35, 31] = 0
    r[35, 34] = 0
    r[35, 38] = 0
    r[36, 27] = 0
    r[36, 40] = 0
    r[37, 29] = 0
    r[37, 33] = 0
    r[37, 34] = 0
    r[37, 41] = 0
    r[38, 30] = 0
    r[38, 34] = 0
    r[38, 35] = 0
    r[38, 42] = 0
    r[39, 32] = 0
    r[39, 43] = 0
    r[40, 36] = 0
    r[40, 41] = 0
    r[41, 40] = 0
    r[41, 37] = 0
    r[42, 38] = 0
    r[42, 43] = 0
    r[43, 39] = 0
    r[43, 42] = 0

    return r

r = initiaR()
for i in range(44):
    for j in range(44):
        if r[i,j] != -1:
            r[i,j] = 1

#print(r)

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

# 验证
q1 = q
for i in range(10):
    q = q1
    print("第{}次验证".format(i + 1))
    state1 = random.randint(0,43)
    print('机器人处于{}'.format(state1))

    q_max = q[state1].max()  # 状态state这一行里的最大值，是一个数值
    q_max_action = []
    for action in range(44):
        if q[state1, action] == q_max:
            q_max_action.append(action)
    next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
    print("the robot goes to " + str(next_state) + '.')
    q[:, state1] = 0
    state = next_state

    count = 0
    while state != state1:  # 回到原点
        if count > 45:
            print('fail')
            break
        # 选择最大的q_max
        q_max = q[state].max()  # 状态state这一行里的最大值，是一个数值

        q_max_action = []
        for action in range(44):
            if q[state, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        print("the robot goes to " + str(next_state) + '.')
        q[:, state] = 0
        state = next_state
        count += 1
