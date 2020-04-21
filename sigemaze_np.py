#-*- codeing = utf-8 -*-
#@Time : 2020/3/30 14:50
#@Author : liuyi
#@File : sigemaze_np.py
#@Software : PyCharm


'''
最简单的四个格子的迷宫
---------------
| start |     |
---------------
|  die  | end |
---------------

每个格子是一个状态，此时都有上下左右停5个动作
'''

# 作者：hhh5460
# 时间：20181218

import numpy as np

epsilon = 0.9  # 贪婪度 greedy
alpha = 0.1  # 学习率
gamma = 0.8  # 奖励递减值

states = range(4)  # 0, 1, 2, 3 四个状态
actions = list('udlrn')  # 上下左右停 五个动作
rewards = [0, 0, -10, 10]  # 奖励集。到达位置3（出口）奖励10，位置2（陷阱）奖励-10，其他皆为0

# 给numpy数组的列加标签，参考https://cloud.tencent.com/developer/ask/72790
q_table = np.zeros(shape=(4,),  # 坑二：这里不能是(4,5)!!
                   dtype=list(zip(actions, ['float'] * 5)))


# dtype=[('u',float),('d',float),('l',float),('r',float),('n',float)])
# dtype={'names':actions, 'formats':[float]*5})

def get_next_state(state, action):
    '''对状态执行动作后，得到下一状态'''
    # u,d,l,r,n = -2,+2,-1,+1,0
    if state % 2 != 1 and action == 'r':  # 除最后一列，皆可向右(+1)
        next_state = state + 1
    elif state % 2 != 0 and action == 'l':  # 除最前一列，皆可向左(-1)
        next_state = state - 1
    elif state // 2 != 1 and action == 'd':  # 除最后一行，皆可向下(+2)
        next_state = state + 2
    elif state // 2 != 0 and action == 'u':  # 除最前一行，皆可向上(-2)
        next_state = state - 2
    else:
        next_state = state
    return next_state


def get_valid_actions(state):
    '''取当前状态下的合法动作集合，与reward无关！'''
    global actions  # ['u','d','l','r','n']

    valid_actions = set(actions)
    if state % 2 == 1:  # 最后一列，则
        valid_actions = valid_actions - set(['r'])  # 去掉向右的动作
    if state % 2 == 0:  # 最前一列，则
        valid_actions = valid_actions - set(['l'])  # 去掉向左
    if state // 2 == 1:  # 最后一行，则
        valid_actions = valid_actions - set(['d'])  # 去掉向下
    if state // 2 == 0:  # 最前一行，则
        valid_actions = valid_actions - set(['u'])  # 去掉向上
    return list(valid_actions)


for i in range(1000):
    # current_state = states[0] # 固定
    current_state = np.random.choice(states, 1)[0]
    while current_state != 3:
        if (np.random.uniform() > epsilon) or (
        (np.array(list(q_table[current_state])) == 0).all()):  # q_table[current_state]是numpy.void类型，只能这么操作！！
            current_action = np.random.choice(get_valid_actions(current_state), 1)[0]
        else:
            current_action = actions[
                np.array(list(q_table[current_state])).argmax()]  # q_table[current_state]是numpy.void类型，只能这么操作！！
        next_state = get_next_state(current_state, current_action)
        next_state_q_values = [q_table[next_state][action] for action in get_valid_actions(next_state)]
        q_table[current_state][current_action] = rewards[next_state] + gamma * max(next_state_q_values)
        current_state = next_state

print('Final Q-table:')
print(q_table)