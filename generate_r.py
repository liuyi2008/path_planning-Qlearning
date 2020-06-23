import numpy
import json

class line(object):

    def  __init__(self,size):
        self.size=size
        self.line=None
        self.matrix=None

    def lineOrMatrix(self,flag=True):
        '''
        是行还是整个矩阵,默认行
        '''
        if flag:
            self.line=numpy.array(list([0]*self.size))
            self.shape=self.line.shape
        else:
            newLine=['0']*self.size
            matrix=[newLine]*self.size
            self.matrix=numpy.array(matrix)
            self.shape=self.matrix.shape

    def makeOne(self,start=None,index=None):
        '''
        将连接的点数置位
        '''
        
        maxNu=index if index else self.size
        zoer=start if start else 0
        for i in range(zoer,maxNu):
            st=input("请输入{}个点所连接的其他的点(以','分隔)".format(i))
            nu=[int(ind) for ind in st.split(",")]
            for px in nu:
                self.matrix[i][px]='1'
            with open("cahce.csv","a",encoding="utf-8") as op:
                op.write(",".join(self.matrix[i])+"\n")
        print("输出为")


    def loadCSv(self):
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

    def save(self):
        '''
        存储为json文件
        :return:
        '''
        saveDist={}
        svaeDist['width']=self.shape[0] #宽
        saveDist['height']=self.shape[1] if self.shape[1] else 1 #长
        cacheDist={}
        for i in range(len(self.matrix)):
            cacheDist[i]=self.matrix[i]
        saveDist["data"]=cacheDist
        with open("matrix.json",'w',encoding="utf-8",) as op:
            json.dump(op,saveDist,ensure_ascii=False)





def start():
    '''
    开始
    '''
    # print("维度")
    # size=int(input())
    # print("行（0）还是矩阵（1）")
    # flag=True if int(input()) == 0 else False
    # one=line(size)
    # one.lineOrMatrix(flag)
    # linke=int(input("是否设置最大上限点数（0否1是）"))
    # if linke==0:
    #     print("未赋值前的矩阵\n",one.matrix)
    #     start=int(input("是否从断点处继续{}"))
    #     one.makeOne(start=start)
    #     print("值前后矩阵\n",one.matrix)
    # one.save()
    # return one.matrix
    one =line(73)
    matrix=one.loadCSv()
    print(matrix.shape,"\n",matrix[2])
    

if __name__=="__main__":
    start()
