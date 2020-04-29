# -*- codeing = utf-8 -*-
# @Time : 2020/4/22 18:04
# @Author : liuyi
# @File : draw.py
# @Software : PyCharm

import turtle
import math
'''
turtle.hideturtle()
turtle.screensize()
#turtle.pencolor('black')
turtle.color('black', 'black')

turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.mainloop()
#turtle.point(5,5)


class Point:
    x = 0
    y = 0


blank = Point()

pp = []
for i in range(6):
    for j in range(6):
        blank.x = j*5
        blank.y = -i*5
        p = [blank.x, blank.y]
        pp.append(p)
print(pp)
print(type(pp))
turtle.pendown()
turtle.goto(pp[1])
turtle.goto(pp[2])
turtle.goto(pp[14])
turtle.goto(pp[13])
turtle.goto(pp[7])
turtle.goto(pp[8])

distance = math.sqrt((pp[1]-pp[8])**2 + (pp[1]-pp[8])**2)

turtle.write(distance)
'''
'''
x1,y1=100,100

x2,y2=100,-100

x3,y3=-100,-100

x4,y4=-100,100

#绘制折线
p = [[100,100],[100,-100],[-100,-100],[-100,100]]

turtle.penup()

turtle.goto(p[0][0], p[0][1])

turtle.pendown()

turtle.goto(x2,y2)

turtle.goto(x3,y3)

turtle.goto(x4,y4)
'''


def drawPoint(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()


def drawLine(x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def drawLines(s = []):
    print(s[1])



drawPoint(0,0)
drawLine(0,0,0,200)
drawPoint(0,200)


x = 0
y = 0
s = []
p = []
for i in range(6):
    for j in range(6):
        x = j*50
        y = -i*50
        drawPoint(x, y)
        p = [x,y]
        s.append(p)


s1 = []

turtle.mainloop()
