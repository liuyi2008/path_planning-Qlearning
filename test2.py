#-*- codeing = utf-8 -*-
#@Time : 2020/3/31 10:47
#@Author : liuyi
#@File : test2.py
#@Software : PyCharm
import numpy as np
import random

r = np.array([[-1, -1, -1, -1, -0, -1], [-1, -1, -1, -0, -1, 100], [-1, -1, -1, -0, -1, -1], [-1, -0, -0, -1, -0, -1],
              [-0, -1, -1, -0, -1, 100], [-1, -0, -1, -1, -0, 100]])

q = np.zeros([6,6],dtype=np.float32)

p = r+1
print(q)
#print(r[2])
r[2]+=4
#print(r[2])
#print(p)
# print(r.any())
# print(q.any())
# print(r.all())
# print((q+1).all())
r = np.array([[-1, -1, -1, -1, -0, -1], [0, 0, 0, 0, 0, 0],[0,0,0,0,0,8]])
#if not r[1].any():
#    print("1")
#print(r[:,3].any())
# print(r[0].any())
# print(r[1].any())
# print(r[2].any())
# print(r[0])
# print(r[1])
# print(r[2])
# if r[1].any():
#     print("全是0")
# a =1
# a+1
# print(r[0])
# r[0]=0
# print(r[0])
# print(r[:,5])
# r[:,5]=0
# print(r[:,5])
# print(r)
#print("from {} jump to {}".format(a,a+1))
# state = 1
# next_state_list=[]
# for i in range(6):
#     print("i=",i)
#     print("r[state,i]=",r[state,i])
#     if r[state, i] != -1:
#         next_state_list.append(i)
# print(next_state_list)

#q_max = r[state].max()
#print(q_max)
# print(r.any())
# print(q.any())

#a = np.array(range(0,5))
#print(a)
# a = np.array([1,5,7,8,9,11])
# for b in a:
#     print(b)
'''
i = 1
j = 2
if i != -1 and j != -1:
    pass
else:
    print("2")
'''
#import this




