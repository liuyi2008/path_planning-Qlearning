# -*- codeing = utf-8 -*-
# @Time : 2020/5/20 17:52
# @Author : liuyi
# @File : v5_point.py
# @Software : PyCharm

# 4度点奖赏调低

import numpy as np
import random
np.set_printoptions(threshold = 1e6)


# -1不通 实验旅行商问题的图
def initiaR2():
    r = np.ones((5, 5), dtype=np.float32)
    r = r * (-1)

    r[0,1] = 18
    r[0,3] = 13
    r[0,4] = 12

    r[1,0] = 18
    r[1,2] = 18
    r[1,3] = 11
    r[1,4] = 16

    r[2,1] = 18
    r[2,3] = 17
    r[2,4] = 18

    r[3,0] = 13
    r[3,1] = 11
    r[3,2] = 17
    r[3,4] = 1

    r[4,0] = 12
    r[4,1] = 16
    r[4,2] = 18
    r[4,3] = 1

    return r


def main():
    print("...................learning.......................")
    q = Qlearning()
    #print("...................寻找路径.......................")
    # for i in range(5):
    #     start = random.randint(0, 41)
    #     print("it's ",i+1,"st path,start with",start)
    #     q1 = q.copy()
    #     findPath(start, q1)
    #     print("....................................................")
#  想法：训练好现有的Q，每一个点都走一遍，然后在选一个最优的
    jumptime = []
    print(".................finding best path.......................")
    for i in range(q.shape[0]):
        q1 = q.copy()
        jumptime.append(find_num_Path(i, q1))
    start = findIndex(min(jumptime),jumptime)
    findPath(start,q)
    print(jumptime)


#  训练过程
def Qlearning():
    #r = initiaR()
    r = initiaR2()

    digit = r.shape[0]

    q = np.zeros([digit, digit], dtype=np.float32)

    gamma = 0.8

    for step in range(1000):
        state = random.randint(0, digit-1)
        for j in range(digit):
            next_state_list = []
            for i in range(digit):
                if r[state, i] != -1:
                    next_state_list.append(i)
            next_state = next_state_list[random.randint(0, len(next_state_list) - 1)]
            qval = r[state, next_state] + gamma * max(q[next_state])  # 注意qval是一个数值
            q[state, next_state] = qval
            state = next_state

    return q


#  找到值在表中的序数,从0开始的
def findIndex(value, list):
    for i in range(len(list)):
        if value == list[i]:
            return i
    return False


#  以起点为start的一条路径
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

        #next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        next_state = q_max_action[0]
        print("the robot goes to " + str(next_state) + '.')
        q[state, next_state] = 0
        q[next_state, state] = 0

        #特意为旅行商问题做的条件
        #q[state] = 0
        #q[:,state] = 0

        #。。。。。。。。。。。。。。。。去掉回头路
        # for next in range(linenum):
        #     if q[state,next] != 0:
        #         q[next_state,next] = 0
        # q[state] = 0  # 和点不一样的地方，边只能经过一次
        # q[:,state] = 0

        state = next_state


def find_num_Path(start, q):
    jumpnum = 0
    linenum = q.shape[0]
    state = start
    #print("robot start at {}".format(state))
    while q.any():

        if not q[state].any():  # 如果此state全是0,就遍历找一个不全是0的state,肯定能找到
            for new_state in range(linenum):
                if not q[new_state].any():
                    continue
                #print("from {} jump to {}".format(state, new_state))
                state = new_state
                jumpnum+=1
                break

        q_max = q[state].max()  # 状态state这一行里的最大值，即回报最大的动作的回报值
        q_max_action = []

        for action in range(linenum):  # 找回报最大的动作的下标
            if q[state, action] == q_max:
                q_max_action.append(action)

        #next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        next_state = q_max_action[0]
        #print("the robot goes to " + str(next_state) + '.')
        q[state, next_state] = 0
        q[next_state, state] = 0
        state = next_state
    return jumpnum


if __name__ == "__main__":  # 整个程序的入口
    main()