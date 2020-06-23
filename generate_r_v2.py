import os

import numpy
import json

# class line(object):
#
#     def __init__(self,size):
#         self.size=size
#         self.line=None
#         self.matrix=None
#
#     def lineOrMatrix(self,flag=True):
#         '''
#         是行还是整个矩阵,默认行
#         '''
#         if flag:
#             self.line=numpy.array(list([0]*self.size))
#         else:
#             newLine=['0']*self.size
#             matrix=[newLine]*self.size
#             self.matrix=numpy.array(matrix)
#
#     def makeOne(self,start=None,index=None):
#         '''
#         将连接的点数置位
#         '''
#
#         maxNu=index if index else self.size#
#         zoer=start if start else 0 #
#         for i in range(zoer,maxNu):
#             st=input("请输入{}个点所连接的其他的点(以','分隔)".format(i))
#             nu=[int(ind) for ind in st.split(",")]
#             for px in nu:
#                 self.matrix[i][px]='1'
#             with open("cahce.csv","a",encoding="utf-8") as op:
#                 op.write(",".join(self.matrix[i])+"\n")
#         print("输出为")
#
#
#     def loadCSv(self):
#         '''
#         从csv文件中读取数据
#         :return:
#         '''
#         data=[]
#         with open("cahce.csv",'r',encoding="utf-8") as op:
#             line=op.readline()
#             while line:
#                 data.append([int(i) for i in line.strip().split(",")])
#                 line=op.readline()
#         return numpy.array(data)
#
#
#
#
#
# def start():
#     '''
#     开始
#     '''
#     # print("维度")
#     # size=int(input())
#     # print("行（0）还是矩阵（1）")
#     # flag=True if int(input()) == 0 else False
#     # one=line(size)
#     # one.lineOrMatrix(flag)
#     # linke=int(input("是否设置最大上限点数（0否1是）"))
#     # if linke==0:
#     #     print("未赋值前的矩阵\n",one.matrix)
#     #     start=int(input("是否从断点处继续{}"))
#     #     one.makeOne(start=start)
#     #     print("值前后矩阵\n",one.matrix)
#     # one.save()
#     # return one.matrix
#     one =line(73)
#     matrix=one.loadCSv()
#     print(matrix.shape,matrix)
#     V1.0


def matrixInit():
    '''
    初始化一个矩阵
    :return:返回初始化后的矩阵
    '''
    while True:
        try:
            dime=int(eval(input("请输入需要连接点的个数")))
            break
        except Exception:
            print("请输入正确的个数值（整数）")
    line=[0]*dime
    matrix=numpy.array([line]*dime)
    return matrix


def makeLine(MATRIX):
    '''
    矩阵输入值
    :param MATRIX:初始化好的点矩阵
    :return:
    '''
    for line in range(len(MATRIX)):
        pointWeight = {}
        while True:
            st=str(input("清输入{}点连接的其他点（以逗号分割，如果存在连接权值请用‘：’设置,不存在默认设为1，如：1,5:6,8:9）".format(line)))
            try:
                point=st.split(",")
                for one in point:
                    cache=one.split(":")
                    column=int(cache[0])
                    if column==line: raise Exception("出错，不可以本身连接")
                    pointWeight[column]=1 if len(cache)==1 else int(cache[1]) #为了防止输入出错加了一些异常处理
                break
            except Exception as p:
                print(p.args)
                print("请输入正确的连接点信息")
        for colu,weight in pointWeight.items():
            MATRIX[line,colu]=weight
        with open("cahce.csv",'a',encoding="utf-8") as op:
            op.write(','.join([str(st) for st in MATRIX[line]])+"\n")
            print("已写入点为{}连接数据".format(line))
    return MATRIX

def loadCsv():
        '''
        从csv文件中读取数据
        :return:
        '''
        data=[]
        with open("cahce.csv",'r',encoding="utf-8") as op:
            line=op.readline()
            while line:
                data.append([int(i) for i in line.strip().split(",")])
                line=op.readline()
        return numpy.array(data)

def start():
    '''
    开始
    :return:
    '''
    if os.path.isfile("oular.csv"):
        choose=str(input("已存在生成好的点连接文件是否生成新的点连接文件？y/n"))
        if str(choose).upper()=='Y':
            with open("cahce.csv",'w'):#想要重新生成一个点连接矩阵的话，需要选择此项
                newMatrix=matrixInit()
            return makeLine(newMatrix)
        elif str(choose).upper()=="N":
            # return loadCsv() #这将会得到直接的矩阵数据
            print(loadCsv())
        else :
            print("？？") #错误输入选择，直接结束程序
    else:
        return makeLine(matrixInit()) #获得点连接数据的两个途径，一个读取CSV文件，一个自己手动输入，之后会返回一个输入成功的矩阵


if __name__=="__main__":
    start()
