# -*- codeing = utf-8 -*-
# @Time : 2020/6/3 17:49
# @Author : liuyi
# @File : v6_addFleury_point.py
# @Software : PyCharm

import numpy as np
import random
import json

stk = [0] * 1000
path = []
top = 0
q = np.ones((5, 5), dtype=np.float32)

'''
r = np.array([
    [0,1,1,0,0,0],
    [1,0,1,0,0,0],
    [1,1,0,1,0,0],
    [0,0,1,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0]
])

r = np.array([
    [0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0]
])
'''

class line(object):

    def __init__(self, size):
        self.size = size
        self.line = None
        self.matrix = None

    def lineOrMatrix(self, flag=True):
        '''
        是行还是整个矩阵,默认行
        '''
        if flag:
            self.line = np.array(list([0] * self.size))
            self.shape = self.line.shape
        else:
            newLine = ['0'] * self.size
            matrix = [newLine] * self.size
            self.matrix = np.array(matrix)
            self.shape = self.matrix.shape

    def makeOne(self, start=None, index=None):
        '''
        将连接的点数置位
        '''

        maxNu = index if index else self.size
        zoer = start if start else 0
        for i in range(zoer, maxNu):
            st = input("请输入{}个点所连接的其他的点(以','分隔)".format(i))
            nu = [int(ind) for ind in st.split(",")]
            for px in nu:
                self.matrix[i][px] = '1'
            with open("cahce.csv", "a", encoding="utf-8") as op:
                op.write(",".join(self.matrix[i]) + "\n")
        print("输出为")

    def loadCSv(self):
        '''
        从csv文件中读取数据
        :return:
        '''
        data = []
        with open("cahce.csv", 'r', encoding="utf-8") as op:
            line = op.readline()
            while line:
                data.append([int(i) for i in line.strip().split(",")])
                line = op.readline()
        return np.array(data)

    def save(self):
        '''
        存储为json文件
        :return:
        '''
        saveDist = {}
        svaeDist['width'] = self.shape[0]  # 宽
        saveDist['height'] = self.shape[1] if self.shape[1] else 1  # 长
        cacheDist = {}
        for i in range(len(self.matrix)):
            cacheDist[i] = self.matrix[i]
        saveDist["data"] = cacheDist
        with open("matrix.json", 'w', encoding="utf-8", ) as op:
            json.dump(op, saveDist, ensure_ascii=False)

one = line(73)
r = one.loadCSv()
N = r.shape[0]  # 点的个数

def dfs(x):  # 去掉break就是正宗的dfs算法
    global top
    stk[top] = x
    top += 1  # 这两句就当是入栈操作

    # for i in range(N):
    #     if q[x, i]:
    #         q[x, i] = q[i, x] = 0
    #         dfs(i)
    #         break

    while q[x].any():
        q_max = q[x].max()  # 状态state这一行里的最大值，即回报最大的动作的回报值
        q_max_action = []

        for action in range(N):  # 找回报最大的动作的下标
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
            if q[stk[top - 1], i]:
                brige = 0
                break

        if brige:
            top -= 1
            print(stk[top])
        else:
            top -= 1
            dfs(stk[top])


def Qlearning():
    # r = initiaR()
    # r = initiaR2()

    digit = r.shape[0]

    for i in range(digit):
        for j in range(digit):
            if r[i,j] == 0:
                r[i,j] = -1
    print(r)

    q = np.zeros([digit, digit], dtype=np.float32)

    gamma = 0.8

    for step in range(1000):
        state = random.randint(0, digit - 1)
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

        # next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        next_state = q_max_action[0]
        print("the robot goes to " + str(next_state) + '.')
        q[state, next_state] = 0
        q[next_state, state] = 0

        # 特意为旅行商问题做的条件
        # q[state] = 0
        # q[:,state] = 0

        # 。。。。。。。。。。。。。。。。去掉回头路
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
    # print("robot start at {}".format(state))
    while q.any():

        if not q[state].any():  # 如果此state全是0,就遍历找一个不全是0的state,肯定能找到
            for new_state in range(linenum):
                if not q[new_state].any():
                    continue
                # print("from {} jump to {}".format(state, new_state))
                state = new_state
                jumpnum += 1
                break

        q_max = q[state].max()  # 状态state这一行里的最大值，即回报最大的动作的回报值
        q_max_action = []

        for action in range(linenum):  # 找回报最大的动作的下标
            if q[state, action] == q_max:
                q_max_action.append(action)

        # next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        next_state = q_max_action[0]
        # print("the robot goes to " + str(next_state) + '.')
        q[state, next_state] = 0
        q[next_state, state] = 0
        state = next_state
    return jumpnum


def main():
    global N
    N = r.shape[0]
    global q
    q = Qlearning()
    print(q)
    fleury(3)

    # print("...................learning.......................")
    # q = Qlearning()
    # jumptime = []
    # print(".................finding best path.......................")
    # for i in range(q.shape[0]):
    #     q1 = q.copy()
    #     jumptime.append(find_num_Path(i, q1))
    # start = findIndex(min(jumptime), jumptime)
    # findPath(start, q)
    # print(jumptime)


if __name__ == "__main__":  # 整个程序的入口
    main()
