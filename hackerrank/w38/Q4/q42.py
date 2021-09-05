filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import bisect

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

class KeyifyList(object):
    def __init__(self, inner, key):
        self.inner = inner
        self.key = key

    def __len__(self):
        return len(self.inner)

    def __getitem__(self, k):
        return self.key(self.inner[k])


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
nodeOrd =[]

def addNodeOrd(node):
    global nodeOrd
    i =  bisect.bisect_left(KeyifyList(nodeOrd,lambda x:x[1]),node[1])
    nodeOrd = nodeOrd[:i] + [node] + nodeOrd[i:]

def removeNodeOrd(node):
    global nodeOrd
    print "Before:" 
    print nodeOrd
    i = bisect.bisect_left(KeyifyList(nodeOrd,lambda x:x[0]),node[0])
    nodeOrd = nodeOrd[:i] + nodeOrd[i+1:]
    print nodeOrd

def updateNodOrd(node):
    global nodeOrd
    i = bisect.bisect_left(KeyifyList(nodeOrd,lambda x:x[0]),node[0])
    if len(nodeOrd)==0:
        addNodeOrd(node)
        return
    if nodeOrd[i][0] != node[0]:
        addNodeOrd(node)
    else:
        removeNodeOrd(node)
        addNodeOrd(node)

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
    global nodes,dic1,nodeOrd
    i= bisect.bisect_left(KeyifyList(nodes[x][1],lambda x:x[0]),w)
    nodes[x][1]= nodes[x][1][:i] +[[w,[w]]] +nodes[x][1][i:]
    if nodes[x][0]<w:
        nodes[x][0] = w
        updateNodOrd([x,w])
    dic1[x] =1

def addToMaxNode(x,w):
    global nodes,dic1
    dic1[x] =1
    if len(nodes[x][1]) ==0:
        nodes[x][1].append([w,[w]])
        nodes[x][0] =w
    else:
        nodes[x][1][-1][1].append(w)
        nodes[x][1][-1][0] = nodes[x][1][-1][0] +w
        nodes[x][0] = nodes[x][0] +w
    updateNodOrd([x,nodes[x][0]])


def removeFromNode(x):
    global nodes,dic1
    y =nodes[x][1][-1][1].pop()
    nodes[x][1][-1][0] = nodes[x][1][-1][0]
    node = nodes[x][1].pop()
    node[0] = node[0] -y
    if node[0] != 0:
        i= bisect.bisect_left(KeyifyList(nodes[x][1],lambda x:x[0]),node[0])
        nodes[x][1]= nodes[x][1][:i] +[node] +nodes[x][1][i:]
    if len(nodes[x][1]) ==0:
        nodes[x][0] =0
    else:
        nodes[x][0] = nodes[x][1][-1][0]
    if nodes[x][0] == 0:
        del dic1[x]
    if nodes[x][0] == 0:
        removeNodeOrd([x,0])
    else:
        updateNodOrd([x,nodes[x][0]])




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



print nodes
print dic1
print nodeOrd