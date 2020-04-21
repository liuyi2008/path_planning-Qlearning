#-*- codeing = utf-8 -*-
#@Time : 2020/3/30 11:41
#@Author : liuyi
#@File : maze.py
#@Software : PyCharm

import pandas as pd
import random
import time
import pickle
import pathlib
import os
import tkinter as tk

'''
 6*6 的迷宫：
-------------------------------------------
| 入口 | 陷阱 |      |      |      |      |
-------------------------------------------
|      | 陷阱 |      |      | 陷阱 |      |
-------------------------------------------
|      | 陷阱 |      | 陷阱 |      |      |
-------------------------------------------
|      | 陷阱 |      | 陷阱 |      |      |
-------------------------------------------
|      | 陷阱 |      | 陷阱 | 元宝 |      |
-------------------------------------------
|      |      |      | 陷阱 |      | 出口 |
-------------------------------------------

作者：hhh5460
时间：20181219
地点：Tai Zi Miao
'''


class Maze(tk.Tk):
    '''环境类（GUI）'''
    UNIT = 40  # pixels
    MAZE_H = 6  # grid height
    MAZE_W = 6  # grid width

    def __init__(self):
        '''初始化'''
        super().__init__()
        self.title('迷宫')
        h = self.MAZE_H * self.UNIT
        w = self.MAZE_W * self.UNIT
        self.geometry('{0}x{1}'.format(h, w))  # 窗口大小
        self.canvas = tk.Canvas(self, bg='white', height=h, width=w)
        # 画网格
        for c in range(0, w, self.UNIT):
            self.canvas.create_line(c, 0, c, h)
        for r in range(0, h, self.UNIT):
            self.canvas.create_line(0, r, w, r)
        # 画陷阱
        self._draw_rect(1, 0, 'black')
        self._draw_rect(1, 1, 'black')
        self._draw_rect(1, 2, 'black')
        self._draw_rect(1, 3, 'black')
        self._draw_rect(1, 4, 'black')
        self._draw_rect(3, 2, 'black')
        self._draw_rect(3, 3, 'black')
        self._draw_rect(3, 4, 'black')
        self._draw_rect(3, 5, 'black')
        self._draw_rect(4, 1, 'black')
        # 画奖励
        self._draw_rect(4, 4, 'yellow')
        # 画玩家(保存!!)
        self.rect = self._draw_rect(0, 0, 'red')
        self.canvas.pack()  # 显示画作！

    def _draw_rect(self, x, y, color):
        '''画矩形，  x,y表示横,竖第几个格子'''
        padding = 5  # 内边距5px，参见CSS
        coor = [self.UNIT * x + padding, self.UNIT * y + padding, self.UNIT * (x + 1) - padding,
                self.UNIT * (y + 1) - padding]
        return self.canvas.create_rectangle(*coor, fill=color)

    def move_to(self, state, delay=0.01):
        '''玩家移动到新位置，根据传入的状态'''
        coor_old = self.canvas.coords(self.rect)  # 形如[5.0, 5.0, 35.0, 35.0]（第一个格子左上、右下坐标）
        x, y = state % 6, state // 6  # 横竖第几个格子
        padding = 5  # 内边距5px，参见CSS
        coor_new = [self.UNIT * x + padding, self.UNIT * y + padding, self.UNIT * (x + 1) - padding,
                    self.UNIT * (y + 1) - padding]
        dx_pixels, dy_pixels = coor_new[0] - coor_old[0], coor_new[1] - coor_old[1]  # 左上角顶点坐标之差
        self.canvas.move(self.rect, dx_pixels, dy_pixels)
        self.update()  # tkinter内置的update!
        time.sleep(delay)


class Agent(object):
    '''个体类'''

    def __init__(self, alpha=0.1, gamma=0.9):
        '''初始化'''
        self.states = range(36)  # 状态集。0~35 共36个状态
        self.actions = list('udlr')  # 动作集。上下左右  4个动作
        self.rewards = [0, -10, 0, 0, 0, 0,
                        0, -10, 0, 0, -10, 0,
                        0, -10, 0, -10, 0, 0,
                        0, -10, 0, -10, 0, 0,
                        0, -10, 0, -10, 3, 0,
                        0, 0, 0, -10, 0, 10, ]  # 奖励集。出口奖励10，陷阱奖励-10，元宝奖励5
        self.hell_states = [1, 7, 13, 19, 25, 15, 31, 37, 43, 10]  # 陷阱位置

        self.alpha = alpha
        self.gamma = gamma

        self.q_table = pd.DataFrame(data=[[0 for _ in self.actions] for _ in self.states],
                                    index=self.states,
                                    columns=self.actions)

    def save_policy(self):
        '''保存Q table'''
        with open('q_table.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self.q_table, f, pickle.HIGHEST_PROTOCOL)

    def load_policy(self):
        '''导入Q table'''
        with open('q_table.pickle', 'rb') as f:
            self.q_table = pickle.load(f)

    def choose_action(self, state, epsilon=0.8):
        '''选择相应的动作。根据当前状态，随机或贪婪，按照参数epsilon'''
        # if (random.uniform(0,1) > epsilon) or ((self.q_table.ix[state] == 0).all()):  # 探索
        if random.uniform(0, 1) > epsilon:  # 探索
            action = random.choice(self.get_valid_actions(state))
        else:
            # action = self.q_table.ix[state].idxmax() # 利用 当有多个最大值时，会锁死第一个！
            # action = self.q_table.ix[state].filter(items=self.get_valid_actions(state)).idxmax() # 重大改进！然鹅与上面一样
            s = self.q_table.ix[state].filter(items=self.get_valid_actions(state))
            action = random.choice(s[s == s.max()].index)  # 从可能有多个的最大值里面随机选择一个！
        return action

    def get_q_values(self, state):
        '''取给定状态state的所有Q value'''
        q_values = self.q_table.ix[state, self.get_valid_actions(state)]
        return q_values

    def update_q_value(self, state, action, next_state_reward, next_state_q_values):
        '''更新Q value，根据贝尔曼方程'''
        self.q_table.ix[state, action] += self.alpha * (
                    next_state_reward + self.gamma * next_state_q_values.max() - self.q_table.ix[state, action])

    def get_valid_actions(self, state):
        '''取当前状态下所有的合法动作'''
        valid_actions = set(self.actions)
        if state % 6 == 5:  # 最后一列，则
            valid_actions -= set(['r'])  # 无向右的动作
        if state % 6 == 0:  # 最前一列，则
            valid_actions -= set(['l'])  # 无向左
        if state // 6 == 5:  # 最后一行，则
            valid_actions -= set(['d'])  # 无向下
        if state // 6 == 0:  # 最前一行，则
            valid_actions -= set(['u'])  # 无向上
        return list(valid_actions)

    def get_next_state(self, state, action):
        '''对状态执行动作后，得到下一状态'''
        # u,d,l,r,n = -6,+6,-1,+1,0
        if state % 6 != 5 and action == 'r':  # 除最后一列，皆可向右(+1)
            next_state = state + 1
        elif state % 6 != 0 and action == 'l':  # 除最前一列，皆可向左(-1)
            next_state = state - 1
        elif state // 6 != 5 and action == 'd':  # 除最后一行，皆可向下(+2)
            next_state = state + 6
        elif state // 6 != 0 and action == 'u':  # 除最前一行，皆可向上(-2)
            next_state = state - 6
        else:
            next_state = state
        return next_state

    def learn(self, env=None, episode=1000, epsilon=0.8):
        '''q-learning算法'''
        print('Agent is learning...')
        for i in range(episode):
            current_state = self.states[0]

            if env is not None:  # 若提供了环境，则重置之！
                env.move_to(current_state)

            while current_state != self.states[-1]:
                current_action = self.choose_action(current_state, epsilon)  # 按一定概率，随机或贪婪地选择
                next_state = self.get_next_state(current_state, current_action)
                next_state_reward = self.rewards[next_state]
                next_state_q_values = self.get_q_values(next_state)
                self.update_q_value(current_state, current_action, next_state_reward, next_state_q_values)
                current_state = next_state

                # if next_state not in self.hell_states: # 非陷阱，则往前；否则待在原位
                #    current_state = next_state

                if env is not None:  # 若提供了环境，则更新之！
                    env.move_to(current_state)
            print(i)
        print('\nok')

    def test(self):
        '''测试agent是否已具有智能'''
        count = 0
        current_state = self.states[0]
        while current_state != self.states[-1]:
            current_action = self.choose_action(current_state, 1.)  # 1., 贪婪
            next_state = self.get_next_state(current_state, current_action)
            current_state = next_state
            count += 1

            if count > 36:  # 没有在36步之内走出迷宫，则
                return False  # 无智能

        return True  # 有智能

    def play(self, env=None, delay=0.5):
        '''玩游戏，使用策略'''
        assert env != None, 'Env must be not None!'

        if not self.test():  # 若尚无智能，则
            if pathlib.Path("q_table.pickle").exists():
                self.load_policy()
            else:
                print("I need to learn before playing this game.")
                self.learn(env, episode=1000, epsilon=0.5)
                self.save_policy()

        print('Agent is playing...')
        current_state = self.states[0]
        env.move_to(current_state, delay)
        while current_state != self.states[-1]:
            current_action = self.choose_action(current_state, 1.)  # 1., 贪婪
            next_state = self.get_next_state(current_state, current_action)
            current_state = next_state
            env.move_to(current_state, delay)
        print('\nCongratulations, Agent got it!')


if __name__ == '__main__':
    env = Maze()  # 环境
    agent = Agent()  # 个体（智能体）
    # agent.learn(env, episode=1000, epsilon=0.6) # 先学习
    # agent.save_policy()
    # agent.load_policy()
    agent.play(env)  # 再玩耍

    # env.after(0, agent.learn, env, 1000, 0.8) # 先学
    # env.after(0, agent.save_policy) # 保存所学
    # env.after(0, agent.load_policy) # 导入所学
    # env.after(0, agent.play, env)            # 再玩
    env.mainloop()
