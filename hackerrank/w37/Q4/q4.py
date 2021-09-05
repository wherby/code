filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

dic1 ={}
for i in range(-10000, 50000):
    dic1[i] = 0

mem ={}

def getPair(n,k):
    res = []
    cnt = (10001 - k)/n +1
    start = -(k+ n)/n
    for i in range(start, cnt):
        res.append(i *n + k)
    return res

def makeDir(n,k):
    global dic1, mem
    n,k = normalize(n,k)
    if (n,k) not in mem:
        res = getPair(n,k)
        mem[(n,k)] = res
    else:
        res = mem[(n,k)]
    for i in res:
        dic1[i] =dic1[i] +1

def removeDir(n,k):
    global dic1,mem
    n,k = normalize(n,k)
    res = mem[(n,k)]
    for i in res:
        dic1[i] =dic1[i] -1

def normalize(n,k):
    k=k- k/n*n
    return (n,k)


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
    ls=  ins[index+i].strip().split()
    if ls[0] == "+":
        makeDir(int(ls[1]),int(ls[2]))
    elif ls[0] == "-":
        removeDir(int(ls[1]),int(ls[2]))
    else:
        print dic1[int(ls[1])]
print dic1