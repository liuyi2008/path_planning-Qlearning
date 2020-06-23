# -*- codeing = utf-8 -*-
# @Time : 2020/6/4 11:31
# @Author : liuyi
# @File : test4.py
# @Software : PyCharm

import numpy as np

# stk = [0]* 10
# top = 1
# stk[1] = 1
# print(stk)

q = np.array([
    [0,1,1,0,0,0],
    [1,0,1,0,0,0],
    [1,2,0,1,0,0],
    [0,0,1,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0]
])
stk = [-1] * 10
top = 0


def dfs(x):  # 去掉break就是正宗的dfs算法
    global top
    stk[top] = x
    top += 1  # 这两句就当是入栈操作

    # for i in range(6):
    #     if q[x, i]:
    #         q[x, i] = q[i, x] = 0
    #         dfs(i)
    #         break

    while q[x].any():
        q_max = q[x].max()  # 状态state这一行里的最大值，即回报最大的动作的回报值
        q_max_action = []

        for action in range(6):  # 找回报最大的动作的下标
            if q[x, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[0]
        q[x, next_state] = q[next_state, x] = 0
        dfs(next_state)
        break

def fleury(x):
    brige = 0
    global top
    stk[top] = x
    top += 1
    while top > 0:
        brige = 1

        for i in range(N):
            if r[stk[top - 1], i]:
                brige = 0
                break

        if brige:
            top -= 1
            print(stk[top])
        else:
            top -= 1
            dfs(stk[top])
dfs(2)
print(stk)