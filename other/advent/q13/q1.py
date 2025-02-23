import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


def parser(tls):
    tls =[t.split(",") for t in tls]
    ret = []
    for i in range(3):
        if i<2:
            for a in tls[i]:
                ret.append(int(a.split("+")[1]))
        if i ==2:
            for a in tls[i]:
                ret.append(int(a.split("=")[1]))
    return ret

def minCost(tls):
    x1,y1,x2,y2,x,y = tls 
    mcs = 10**30
    for i in range(x//x1 +1):
        b = (x-i*x1) //x2 
        if i*x1 +b*x2 == x and i*y1 +b*y2 ==y and b >=0:
            mcs = min(mcs,i*3+b)
    return mcs
def solve():
    ls = []
    tmp =[]
    for _ in range(1280):
        a = input()
        if len(a) >1:
            tmp.append(a)
        else:
            ls.append(tmp)
            tmp =[]
    cnt =0
    for tls in ls:
        ret = parser(tls)
        mcs =minCost(ret)
        if mcs <10**30:
            cnt +=mcs
    print(cnt)



solve()