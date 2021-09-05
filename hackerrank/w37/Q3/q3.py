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


def getNum(ls):
    maxN =max(ls)
    cnt =0
    maxNIndex=0
    for i in range(26):
        if maxN == ls[i]:
            maxNIndex =i
    a1 =0
    a2 =0
    for i in range(maxNIndex):
        a1 = a1 + ls[i]
    for i in range(maxNIndex +1 ,26):
        a2 = a2+ ls[i]
    if a1>0:
        cnt = cnt +a1
        maxN =maxN -cnt
    res = max( min(maxN-1,a2 -1), min(maxN, a2-2))

    cnt = cnt + res
    if cnt <0:
        cnt =0
    print cnt

def getSeq(ls):
    n=sum(ls)
    maxN = max(ls)
    if maxN>=n/2:
        getNum(ls)
    else:
        print (n-1)/2

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
    ls = map(int , ins[index+i].strip().split())
    getSeq(ls)