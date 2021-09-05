filename = "input/input00.txt"
f=open(filename,'r')



import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)




n, = map(int , ins[0].strip().split())
ls =  map(int , ins[1].strip().split())
ring= [0]
dis =0
for i in ls:
    ring.append(dis)
    dis = dis +i
ring.append(dis)
nodes = []
for i in range(n +1):
    nodes.append([0,[]])
dic1={}

def getBase(x1,x2):
    global ring,n
    if x1==x2:
        return 0
    if x2>x1:
        return ring[x2]-ring[x1]
    else:
        return ring[n+1]-ring[x1] + ring[x2]

def getTotalDis(x1,x2):
    global nodes
    return getBase(x1,x2) + nodes[x2][0]


def findFarest(x1):
    global nodes,n, dic1
    if x1==1:
        farNode =n
    else:
        farNode = x1 -1
    farWT = getTotalDis(x1,farNode) 
    for key,value in dic1.items():
        tmp = getTotalDis(x1,key)
        if tmp > farWT:
            farWT =tmp
            farNode =key
    return (farNode,farWT)

def addToNode(x,w):
    global nodes,dic1
    nodes[x][1].append([w,[w]])
    if nodes[x][0]<w:
        nodes[x][0] = w
    dic1[x] =1

def addToMaxNode(x,w):
    global nodes,dic1
    dic1[x] =1
    if len(nodes[x][1]) ==0:
        nodes[x][1].append([w,[w]])
        nodes[x][0] =w
    else:
        maxIndex = 0
        maxValue = nodes[x][1][0][0]
        for i in range(len(nodes[x][1])):
            node = nodes[x][1][i]
            if node[0] > maxValue:
                maxValue = node[0]
                maxIndex =i
        nodes[x][1][maxIndex][1].append(w)
        nodes[x][1][maxIndex][0] = nodes[x][1][maxIndex][0] +w
        if nodes[x][1][maxIndex][0] > nodes[x][0]:
            nodes[x][0] = nodes[x][1][maxIndex][0]


def removeFromNode(x):
    global nodes,dic1
    maxIndex = 0
    maxValue = nodes[x][1][0][0]
    for i in range(len(nodes[x][1])):
        node = nodes[x][1][i]
        if node[0] > maxValue:
            maxValue = node[0]
            maxIndex = i
    y=nodes[x][1][maxIndex][1].pop()
    nodes[x][1][maxIndex][0] = nodes[x][1][maxIndex][0] -y
    if nodes[x][1][maxIndex][0] ==0:
        nodes[x][1] = nodes[x][1][:maxIndex] + nodes[x][1][maxIndex+1:]
    if len(nodes[x][1]) ==0:
        nodes[x][0] = 0
        return
    maxIndex = 0
    maxValue = nodes[x][1][0][0]
    for i in range(len(nodes[x][1])):
        node = nodes[x][1][i]
        if node[0] > maxValue:
            maxValue = node[0]
            maxIndex = i
    nodes[x][0] = nodes[x][1][maxIndex][0]




def addToFar(x,w):
    farNode,farWT =findFarest(x)
    addToMaxNode(farNode,w)

def removeFromFar(x):
    farNode,farWT =findFarest(x)
    removeFromNode(farNode)

def printFarV(x):
    farNode,farWT =findFarest(x)
    print(farWT)


q, = map(int , ins[2].strip().split())
index=3
for i in range(q):
    tp=list(map(int , ins[index+i].strip().split()))
    if tp[0] == 1:
        x1,x2,w1 = tp
        addToFar(x2,w1)
    if tp[0]==2:
        x1,x2,w1 = tp
        addToNode(x2,w1)
    if tp[0] ==3:
        x1,x2 =tp
        removeFromFar(x2)
    if tp[0] ==4:
        x1,x2 = tp
        printFarV(x2)