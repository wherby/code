filename = "./input/input00.txt"
f=open(filename,'r')


#https://www.hackerrank.com/contests/w30/challenges/range-modular-queries/editorial

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
from collections import defaultdict as ddic
import bisect

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

def query(arr, left, right):
    jx = bisect.bisect(arr, right)
    ix = bisect.bisect_left(arr, left)
    return jx - ix

def buildSmall(x,ls):
    rec = ddic(list)
    for i,v in enumerate(ls):
        rec[v %x].append(i)
    return rec

k,q = map(int , ins[0].strip().split())
ls=map(int , ins[1].strip().split())
index=2

V = ddic(list)

M = max(ls)
for i,v in enumerate(ls):
    V[v].append(i)

smallRec = {}

MAGIC =100

for i in range(q):
    l,r,x,y= map(int , ins[index+i].strip().split())
    if x <=MAGIC:
        if x not in smallRec:
            smallRec[x] = buildSmall(x,ls)
        print query(smallRec[x][y],l,r)
    else:
        count = 0
        for k in range(y,M+1,x):
            count += query(V[k],l,r)
        print count

