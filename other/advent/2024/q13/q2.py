import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
from math import gcd,lcm
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
    t1,t2 =3,1
    mcs = 10**30
    if x1<=y1:
        x1,y1,x2,y2 = x2,y2,x1,y1
        t1,t2 =1,3
    if x1 < y1:
        return mcs
    a =(x1-y1)
    b = (y2-x2)
    d = lcm(a,b)
    e = d//a *x1 + d//b*x2 
    pp = 10**13
    
    k = pp// e  - abs(x-y)
    res = pp -k*e
    ret = d//a*k*t1 + d//b*k*t2
    x,y = x+res,y+res

    for i in range(x//x1 +1):
        b = (x-i*x1) //x2 
        if i*x1 +b*x2 == x and i*y1 +b*y2 ==y and b >=0:
            mcs = min(mcs,i*t1+b*t2 +ret)
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
        #print(mcs)
        if mcs <10**30:
            cnt +=mcs
    print(cnt)



solve()

# 2278831895 too low
# 6783574783 too low